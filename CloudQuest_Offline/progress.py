import json
import os
from datetime import date

from improved_data import get_lessons

# Path to progress file within this directory
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")

# Enhanced progress structure with Slay the Spire mechanics
DEFAULT_PROGRESS = {
    "xp": 0,
    "streak": 0,
    "last_completed_date": None,
    "energy": 3,  # Energy shields (health in StS)
    "max_energy": 3,
    "badges": [],
    "completed_lessons": [],
    "current_lesson": 1,  # Current map position
    "inventory": {
        "relics": [],  # Permanent upgrades
        "potions": [],  # Consumable bonuses
        "gold": 0,  # Currency for shop purchases
        "cards": [],  # Knowledge cards collected
    },
    "stats": {
        "battles_won": 0,
        "elites_defeated": 0,
        "bosses_defeated": 0,
        "total_questions": 0,
        "correct_answers": 0,
        "streak_best": 0,
        "runs_completed": 0,
    },
    "achievements": [],  # Special accomplishments
    "ascension_level": 0,  # Difficulty modifier like StS
    "character_unlocks": ["zap"],  # Available characters/mascots
    "relic_uses": {},  # Track per-question relic usage to prevent abuse
}


def _init_progress_file():
    """Create the progress file if it does not exist."""
    if not os.path.isfile(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w") as f:
            json.dump(DEFAULT_PROGRESS, f, indent=2)


def load_progress():
    """Load the user's progress from disk."""
    _init_progress_file()
    with open(PROGRESS_FILE, "r") as f:
        progress = json.load(f)

    # Ensure all new fields exist (for backward compatibility)
    for key in DEFAULT_PROGRESS:
        if key not in progress:
            progress[key] = DEFAULT_PROGRESS[key]

    return progress


def save_progress(progress):
    """Persist the progress dictionary to disk."""
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def register_quiz_result(lesson_id, correct, xp_gain_correct=20, xp_gain_incorrect=5):
    """
    Enhanced quiz result processing with Slay the Spire battle mechanics.
    Guardian's Shield is now properly limited.
    """
    progress = load_progress()
    lessons = get_lessons()
    lesson = next((l for l in lessons if l["id"] == lesson_id), None)
    message = ""
    next_lesson_id = lesson_id

    if not lesson:
        return progress, "Invalid lesson", lesson_id

    # Reset relic uses for new question
    question_key = f"lesson_{lesson_id}"
    progress["relic_uses"] = progress.get("relic_uses", {})
    progress["relic_uses"][question_key] = progress["relic_uses"].get(question_key, {})

    # Update stats
    progress["stats"]["total_questions"] += 1

    if correct:
        # Victory! Award XP and restore energy
        progress["xp"] += xp_gain_correct
        progress["energy"] = min(progress["max_energy"], progress.get("energy", 3) + 1)
        progress["stats"]["correct_answers"] += 1

        # Update battle stats based on room type
        room_type = lesson.get("room_type", "battle")
        if room_type == "battle":
            progress["stats"]["battles_won"] += 1
        elif room_type == "elite":
            progress["stats"]["elites_defeated"] += 1
        elif room_type == "boss":
            progress["stats"]["bosses_defeated"] += 1

        # Build success message
        message = f"🎉 Correct! You've earned {xp_gain_correct} XP and restored 1 energy shield!"

        if lesson.get("explanation"):
            message += f"\n\n💡 {lesson['explanation']}"

        # Mark lesson as completed
        if lesson_id not in progress.get("completed_lessons", []):
            progress["completed_lessons"].append(lesson_id)

        # Award badge
        badge_name = lesson.get("badge")
        if badge_name and badge_name not in progress.get("badges", []):
            progress["badges"].append(badge_name)
            message += f"\n🏆 You earned the {badge_name} badge!"

        # Determine next lesson
        next_lesson_id = lesson_id + 1 if lesson_id < len(lessons) else 1

        # Update current lesson progress
        if lesson_id == progress.get("current_lesson", 1):
            progress["current_lesson"] = min(len(lessons), lesson_id + 1)

    else:
        # DEFEAT! Lose energy but gain some participation XP
        old_energy = progress.get("energy", 3)
        progress["energy"] = max(0, old_energy - 1)
        progress["xp"] += xp_gain_incorrect

        message = f"❌ Incorrect answer. You lost 1 shield (now {progress['energy']}/{progress['max_energy']}) but gained {xp_gain_incorrect} XP for trying."

        # Apply Guardian's Shield effect if available and not used for this question
        progress, shield_message = apply_guardian_shield(
            progress, lesson_id, question_key
        )
        if shield_message:
            message += f"\n\n🛡️ {shield_message}"

        # Stay on same lesson for retry
        next_lesson_id = lesson_id

    # Apply other relic effects
    progress = apply_relic_effects(progress, lesson, correct)

    # Check for new achievements
    progress = check_achievements(progress)

    # Clean up old relic usage tracking (keep only last 10 questions)
    if len(progress["relic_uses"]) > 10:
        oldest_keys = list(progress["relic_uses"].keys())[:-10]
        for key in oldest_keys:
            del progress["relic_uses"][key]

    save_progress(progress)
    return progress, message, next_lesson_id


def apply_guardian_shield(progress, lesson_id, question_key):
    """
    Apply Guardian's Shield effect with proper limitations.
    Returns updated progress and message about shield effect.
    """
    relics = progress.get("inventory", {}).get("relics", [])

    # Check if player has Guardian's Shield
    has_guardian_shield = any(
        relic.get("name") == "Guardian's Shield" for relic in relics
    )

    if not has_guardian_shield:
        return progress, ""

    # Check if Guardian's Shield was already used for this question
    shield_used = progress["relic_uses"][question_key].get(
        "guardian_shield_used", False
    )

    if shield_used:
        return progress, ""

    # Check if player has energy to restore (not at 0)
    if progress["energy"] <= 0:
        return progress, ""

    # Apply Guardian's Shield effect - prevent 1 damage (restore the lost shield)
    progress["energy"] = min(progress["max_energy"], progress["energy"] + 1)
    progress["relic_uses"][question_key]["guardian_shield_used"] = True

    shield_message = f"Guardian's Shield activated! Damage prevented. Energy restored to {progress['energy']}/{progress['max_energy']}."

    return progress, shield_message


def apply_relic_effects(progress, lesson, correct):
    """Apply passive effects from collected relics (except Guardian's Shield)"""
    relics = progress.get("inventory", {}).get("relics", [])

    for relic in relics:
        relic_name = relic.get("name", "")

        # CloudWatch Lens: Bonus XP for monitoring questions
        if relic_name == "CloudWatch Lens" and correct:
            if "monitoring" in lesson.get("title", "").lower():
                progress["xp"] += 5

        # Deployment Automation Gem: Extra XP for elite battles
        elif (
            relic_name == "Deployment Automation Gem"
            and lesson.get("room_type") == "elite"
        ):
            progress["xp"] += 10

        # Serverless Scaling Serum: Bonus XP for serverless questions
        elif relic_name == "Serverless Scaling Serum" and correct:
            if (
                "serverless" in lesson.get("title", "").lower()
                or "lambda" in lesson.get("content", "").lower()
            ):
                progress["xp"] += 8

    return progress


def complete_lesson(lesson_id=None, xp_gain=10):
    """Mark a lesson as completed with enhanced Slay the Spire mechanics."""
    progress = load_progress()
    today = date.today().isoformat()

    # Handle streak logic
    if progress.get("last_completed_date") == today:
        progress["streak"] += 1
    else:
        progress["streak"] = 1

    progress["last_completed_date"] = today

    # Update best streak
    if progress["streak"] > progress["stats"]["streak_best"]:
        progress["stats"]["streak_best"] = progress["streak"]

    # Award XP and restore energy
    progress["xp"] += xp_gain
    progress["energy"] = min(progress["max_energy"], progress.get("energy", 3) + 1)

    # Update lesson progression
    if lesson_id:
        if lesson_id not in progress["completed_lessons"]:
            progress["completed_lessons"].append(lesson_id)

        # Advance current lesson if this was the current one
        if lesson_id == progress.get("current_lesson", 1):
            progress["current_lesson"] = lesson_id + 1

    # Check for achievements
    progress = check_achievements(progress)

    save_progress(progress)
    return progress


def check_achievements(progress):
    """Check and award achievements based on progress"""
    achievements = progress.get("achievements", [])
    new_achievements = []

    # Define achievements
    achievement_checks = [
        {
            "id": "first_victory",
            "name": "First Victory",
            "description": "Complete your first lesson",
            "condition": len(progress.get("completed_lessons", [])) >= 1,
        },
        {
            "id": "elite_slayer",
            "name": "Elite Slayer",
            "description": "Defeat 3 elite challenges",
            "condition": progress.get("stats", {}).get("elites_defeated", 0) >= 3,
        },
        {
            "id": "boss_hunter",
            "name": "Boss Hunter",
            "description": "Defeat your first boss",
            "condition": progress.get("stats", {}).get("bosses_defeated", 0) >= 1,
        },
        {
            "id": "knowledge_seeker",
            "name": "Knowledge Seeker",
            "description": "Answer 100 questions",
            "condition": progress.get("stats", {}).get("total_questions", 0) >= 100,
        },
        {
            "id": "perfect_streak",
            "name": "Perfect Streak",
            "description": "Maintain a 7-day learning streak",
            "condition": progress.get("stats", {}).get("streak_best", 0) >= 7,
        },
        {
            "id": "aws_master",
            "name": "AWS Master",
            "description": "Earn all domain badges",
            "condition": len(progress.get("badges", [])) >= 8,
        },
        {
            "id": "relic_collector",
            "name": "Relic Collector",
            "description": "Collect 5 different relics",
            "condition": len(progress.get("inventory", {}).get("relics", [])) >= 5,
        },
        {
            "id": "guardian_saved",
            "name": "Protected by the Guardian",
            "description": "Guardian's Shield saves you from defeat",
            "condition": any(
                relic.get("name") == "Guardian's Shield"
                for relic in progress.get("inventory", {}).get("relics", [])
            ),
        },
    ]

    for achievement in achievement_checks:
        if achievement["id"] not in achievements and achievement["condition"]:
            achievements.append(achievement["id"])
            new_achievements.append(achievement)

    progress["achievements"] = achievements

    # Award bonus XP for new achievements
    for achievement in new_achievements:
        progress["xp"] += 50

    return progress


def use_potion(progress, potion_name):
    """Use a potion from inventory for temporary effects"""
    potions = progress.get("inventory", {}).get("potions", [])

    for i, potion in enumerate(potions):
        if potion.get("name") == potion_name:
            # Apply potion effect
            if "Shield" in potion_name:
                progress["energy"] = progress["max_energy"]  # Full heal
            elif "XP Boost" in potion_name:
                progress["xp"] += 25  # Bonus XP

            # Remove used potion
            potions.pop(i)
            break

    save_progress(progress)
    return progress


def reset_run(progress):
    """Reset for new run (like dying in Slay the Spire)"""
    # Keep persistent progress but reset run-specific items
    progress["energy"] = progress["max_energy"]
    progress["current_lesson"] = 1
    progress["inventory"]["potions"] = []  # Lose potions
    progress["stats"]["runs_completed"] += 1
    progress["relic_uses"] = {}  # Reset relic usage

    # Keep relics and badges (permanent upgrades)
    save_progress(progress)
    return progress


def has_guardian_shield(progress):
    """Check if player has Guardian's Shield relic"""
    relics = progress.get("inventory", {}).get("relics", [])
    return any(relic.get("name") == "Guardian's Shield" for relic in relics)
