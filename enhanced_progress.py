import json
import os
from datetime import date
from improved_data import get_lessons

# Path to progress file within this directory
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), 'progress.json')

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
        "cards": []  # Knowledge cards collected
    },
    "stats": {
        "battles_won": 0,
        "elites_defeated": 0,
        "bosses_defeated": 0,
        "total_questions": 0,
        "correct_answers": 0,
        "streak_best": 0,
        "runs_completed": 0
    },
    "achievements": [],  # Special accomplishments
    "ascension_level": 0,  # Difficulty modifier like StS
    "character_unlocks": ["zap"]  # Available characters/mascots
}

def _init_progress_file():
    """
    Create the progress file if it does not exist.
    """
    if not os.path.isfile(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(DEFAULT_PROGRESS, f, indent=2)

def load_progress():
    """
    Load the user's progress from disk. If the file does not exist
    initialize it with default values.
    """
    _init_progress_file()
    with open(PROGRESS_FILE, 'r') as f:
        progress = json.load(f)

    # Ensure all new fields exist (for backward compatibility)
    for key in DEFAULT_PROGRESS:
        if key not in progress:
            progress[key] = DEFAULT_PROGRESS[key]

    return progress

def save_progress(progress):
    """
    Persist the progress dictionary to disk.
    """
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def complete_lesson(lesson_id=None, xp_gain=10):
    """
    Mark a lesson as completed with enhanced Slay the Spire mechanics.

    Args:
        lesson_id (int): ID of completed lesson
        xp_gain (int): Amount of XP to award.

    Returns:
        dict: Updated progress.
    """
    progress = load_progress()
    today = date.today().isoformat()

    # Handle streak logic
    if progress.get('last_completed_date') == today:
        progress['streak'] += 1
    else:
        progress['streak'] = 1
    progress['last_completed_date'] = today

    # Update best streak
    if progress['streak'] > progress['stats']['streak_best']:
        progress['stats']['streak_best'] = progress['streak']

    # Award XP and restore energy
    progress['xp'] += xp_gain
    progress['energy'] = min(progress['max_energy'], progress.get('energy', 3) + 1)

    # Update lesson progression
    if lesson_id:
        if lesson_id not in progress['completed_lessons']:
            progress['completed_lessons'].append(lesson_id)

        # Advance current lesson if this was the current one
        if lesson_id == progress.get('current_lesson', 1):
            progress['current_lesson'] = lesson_id + 1

    # Check for achievements
    progress = check_achievements(progress)

    save_progress(progress)
    return progress

def register_quiz_result(lesson_id, correct, xp_gain_correct=20, xp_gain_incorrect=5):
    """
    Enhanced quiz result processing with Slay the Spire battle mechanics.

    Args:
        lesson_id (int): ID of the lesson being quizzed.
        correct (bool): Whether the user's answer was correct.
        xp_gain_correct (int): XP to award for correct answer.
        xp_gain_incorrect (int): XP to award for incorrect answer.

    Returns:
        tuple: (progress dict, message str, next_lesson_id)
    """
    progress = load_progress()
    lessons = get_lessons()
    lesson = next((l for l in lessons if l['id'] == lesson_id), None)

    message = ""
    next_lesson_id = lesson_id

    if not lesson:
        return progress, "Invalid lesson", lesson_id

    # Update stats
    progress['stats']['total_questions'] += 1

    if correct:
        # Victory! Award XP and restore energy
        progress['xp'] += xp_gain_correct
        progress['energy'] = min(progress['max_energy'], progress.get('energy', 3) + 1)
        progress['stats']['correct_answers'] += 1

        # Update battle stats based on room type
        room_type = lesson.get('room_type', 'battle')
        if room_type == 'battle':
            progress['stats']['battles_won'] += 1
        elif room_type == 'elite':
            progress['stats']['elites_defeated'] += 1
        elif room_type == 'boss':
            progress['stats']['bosses_defeated'] += 1

        # Build success message with explanation
        message = f"🎉 Correct! You've earned {xp_gain_correct} XP."
        if lesson.get('explanation'):
            message += f"\n\n💡 {lesson['explanation']}"

        # Mark lesson as completed if not already done
        if lesson_id not in progress.get('completed_lessons', []):
            progress['completed_lessons'].append(lesson_id)

            # Award badge for this lesson
            badge_name = lesson.get('badge')
            if badge_name and badge_name not in progress.get('badges', []):
                progress['badges'].append(badge_name)
                message += f"\n🏆 You earned the {badge_name} badge!"

        # Determine next lesson
        next_lesson_id = lesson_id + 1 if lesson_id < len(lessons) else 1

        # Update current lesson progress
        if lesson_id == progress.get('current_lesson', 1):
            progress['current_lesson'] = min(len(lessons), lesson_id + 1)

    else:
        # Defeat! Lose energy but gain some participation XP
        progress['energy'] = max(0, progress.get('energy', 3) - 1)
        progress['xp'] += xp_gain_incorrect

        message = f"❌ Incorrect answer. You lose one shield but gain {xp_gain_incorrect} XP for trying."

        # Stay on same lesson for retry
        next_lesson_id = lesson_id

    # Apply relic effects (passive bonuses from collected relics)
    progress = apply_relic_effects(progress, lesson, correct)

    # Check for new achievements
    progress = check_achievements(progress)

    save_progress(progress)
    return progress, message, next_lesson_id

def apply_relic_effects(progress, lesson, correct):
    """Apply passive effects from collected relics"""
    relics = progress.get('inventory', {}).get('relics', [])

    for relic in relics:
        relic_name = relic.get('name', '')

        # Example relic effects
        if relic_name == "CloudWatch Lens" and correct:
            # Bonus XP for monitoring questions
            if "monitoring" in lesson.get('title', '').lower():
                progress['xp'] += 5

        elif relic_name == "Guardian's Shield":
            # Reduced energy loss on incorrect answers
            if not correct and progress['energy'] < progress['max_energy']:
                progress['energy'] += 1  # Reduce damage by 1

        elif relic_name == "Deployment Automation Gem" and lesson.get('room_type') == 'elite':
            # Extra XP for elite battles
            progress['xp'] += 10

    return progress

def check_achievements(progress):
    """Check and award achievements based on progress"""
    achievements = progress.get('achievements', [])
    new_achievements = []

    # Define achievements
    achievement_checks = [
        {
            'id': 'first_victory',
            'name': 'First Victory',
            'description': 'Complete your first lesson',
            'condition': len(progress.get('completed_lessons', [])) >= 1
        },
        {
            'id': 'elite_slayer',
            'name': 'Elite Slayer', 
            'description': 'Defeat 3 elite challenges',
            'condition': progress.get('stats', {}).get('elites_defeated', 0) >= 3
        },
        {
            'id': 'boss_hunter',
            'name': 'Boss Hunter',
            'description': 'Defeat your first boss',
            'condition': progress.get('stats', {}).get('bosses_defeated', 0) >= 1
        },
        {
            'id': 'knowledge_seeker',
            'name': 'Knowledge Seeker',
            'description': 'Answer 100 questions',
            'condition': progress.get('stats', {}).get('total_questions', 0) >= 100
        },
        {
            'id': 'perfect_streak',
            'name': 'Perfect Streak',
            'description': 'Maintain a 7-day learning streak',
            'condition': progress.get('stats', {}).get('streak_best', 0) >= 7
        },
        {
            'id': 'aws_master',
            'name': 'AWS Master',
            'description': 'Earn all domain badges',
            'condition': len(progress.get('badges', [])) >= 8
        }
    ]

    for achievement in achievement_checks:
        if achievement['id'] not in achievements and achievement['condition']:
            achievements.append(achievement['id'])
            new_achievements.append(achievement)

    progress['achievements'] = achievements

    # Award bonus XP for new achievements
    for achievement in new_achievements:
        progress['xp'] += 50

    return progress

def use_potion(progress, potion_name):
    """Use a potion from inventory for temporary effects"""
    potions = progress.get('inventory', {}).get('potions', [])

    for i, potion in enumerate(potions):
        if potion.get('name') == potion_name:
            # Apply potion effect (implementation depends on potion type)
            if 'Shield' in potion_name:
                progress['energy'] = progress['max_energy']  # Full heal
            elif 'XP Boost' in potion_name:
                progress['xp'] += 25  # Bonus XP

            # Remove used potion
            potions.pop(i)
            break

    save_progress(progress)
    return progress

def reset_run(progress):
    """Reset for new run (like dying in Slay the Spire)"""
    # Keep persistent progress but reset run-specific items
    progress['energy'] = progress['max_energy']
    progress['current_lesson'] = 1
    progress['inventory']['potions'] = []  # Lose potions
    progress['stats']['runs_completed'] += 1

    # Keep relics and badges (permanent upgrades)
    save_progress(progress)
    return progress
