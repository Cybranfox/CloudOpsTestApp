import os
import random
from datetime import date, datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS

from improved_data import get_lessons as _get_aws_lessons
from platforms_data import get_platforms, get_platform, get_platform_progress

# ── Multi-platform lesson registry ────────────────────────────────────────────
# Lesson ID ranges:  1-99 → AWS   |  101-199 → Kubernetes  |  201-299 → Docker
#  301-399 → Ansible  |  401-499 → Terraform
try:
    from kubernetes_data import get_lessons as _get_k8s_lessons
except ImportError:
    _get_k8s_lessons = lambda: []

try:
    from docker_data import get_lessons as _get_docker_lessons
except ImportError:
    _get_docker_lessons = lambda: []

try:
    from ansible_data import get_lessons as _get_ansible_lessons
except ImportError:
    _get_ansible_lessons = lambda: []


def get_lessons():
    """Return all lessons across all active platforms."""
    return (
        _get_aws_lessons()
        + _get_k8s_lessons()
        + _get_docker_lessons()
        + _get_ansible_lessons()
    )


def get_lesson_by_id(lesson_id):
    """Fast single-lesson lookup without loading all lessons."""
    if lesson_id < 100:
        source = _get_aws_lessons
    elif lesson_id < 200:
        source = _get_k8s_lessons
    elif lesson_id < 300:
        source = _get_docker_lessons
    elif lesson_id < 400:
        source = _get_ansible_lessons
    else:
        source = get_lessons  # fallback: scan all
    return next((l for l in source() if l["id"] == lesson_id), None)


# ──────────────────────────────────────────────────────────────────────────────
from progress import (
    check_achievements,
    complete_lesson,
    has_guardian_shield,
    load_progress,
    register_quiz_result,
    save_progress,
)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-insecure-change-me")

CORS(
    app,
    origins=[
        "capacitor://localhost",
        "http://localhost",
        "http://localhost:5001",
    ],
)


# ── Error handlers ─────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


# ─────────────────────────────────────────────────────────────────────────────


# Custom Jinja2 filters
def intersect_filter(list1, list2):
    """Return intersection of two lists"""
    return [item for item in list1 if item in list2]


# Register the filter
app.jinja_env.filters["intersect"] = intersect_filter


@app.route("/")
def home():
    """Enhanced home page with space adventure map"""
    progress = load_progress()
    lessons = get_lessons()
    platforms = get_platforms()

    # Build a lookup of lesson_id -> lesson for quick access
    lesson_map = {l["id"]: l for l in lessons}

    # Build platform-aware map data for the template
    return render_template(
        "space_adventure_map.html",
        progress=progress,
        lessons=lessons,
        platforms=platforms,
        lesson_map=lesson_map,
    )


@app.route("/lesson/<int:lesson_id>")
def lesson_page(lesson_id):
    """Display lesson content before quiz"""
    lesson = get_lesson_by_id(lesson_id)

    if not lesson:
        return "Lesson not found", 404

    progress = load_progress()
    return render_template("lesson.html", lesson=lesson, progress=progress)


@app.route("/quiz/<int:lesson_id>", methods=["GET", "POST"])
def quiz(lesson_id):
    """Handle quiz questions and answers with audio feedback"""
    lesson = get_lesson_by_id(lesson_id)

    if not lesson:
        return "Lesson not found", 404

    progress = load_progress()

    if request.method == "POST":
        # Handle quiz answer submission
        user_answer = request.form.get("option")
        if not user_answer:
            user_answer = request.form.getlist("option")  # For multi-select

        # Check if answer is correct
        if isinstance(lesson.get("answer"), list):
            # Multi-select question
            correct = set(user_answer) == set(lesson["answer"])
        else:
            correct = user_answer == lesson.get("answer")

        # Process the result
        progress, message, next_lesson_id = register_quiz_result(lesson_id, correct)

        # Check for milestone rewards (every 15 questions)
        total_questions = progress.get("stats", {}).get("total_questions", 0)
        if total_questions > 0 and total_questions % 15 == 0:
            return redirect(
                url_for(
                    "reward_screen",
                    milestone_count=total_questions,
                    lesson_id=lesson_id,
                )
            )

        return render_template(
            "quiz.html",
            lesson=lesson,
            progress=progress,
            correct=correct,
            message=message,
            next_lesson_id=next_lesson_id,
            show_result=True,
        )

    # GET request - show the quiz
    return render_template(
        "quiz.html", lesson=lesson, progress=progress, show_result=False
    )


@app.route("/reward/<int:milestone_count>")
def reward_screen(milestone_count):
    """Duolingo-style reward screen every 15 questions"""
    progress = load_progress()

    # Calculate bonus XP for milestone
    bonus_xp = 50 + (milestone_count // 15) * 10
    progress["xp"] += bonus_xp

    # Check for streak milestones
    streak_milestone = progress.get("streak", 0) >= 3
    streak_days = progress.get("streak", 0)

    # Get recent badges (simplified for now)
    new_badges = get_recent_badges(progress)

    # Calculate accuracy
    stats = progress.get("stats", {})
    total_q = stats.get("total_questions", 1)
    correct_q = stats.get("correct_answers", 0)
    accuracy = round((correct_q / total_q) * 100) if total_q > 0 else 0

    # Calculate next challenge
    next_challenge = {
        "name": "AWS Mastery Path",
        "description": "Continue your journey through the AWS galaxy",
        "icon": "🚀",
        "current": milestone_count,
        "target": ((milestone_count // 15) + 1) * 15,
        "progress": ((milestone_count % 15) / 15) * 100,
    }

    # Calculate mastery level
    mastery_level = min(10, len(progress.get("badges", [])))

    save_progress(progress)

    return render_template(
        "reward_screen_orbit.html",
        milestone_count=milestone_count,
        bonus_xp=bonus_xp,
        streak_milestone=streak_milestone,
        streak_days=streak_days,
        new_badges=new_badges,
        current_energy=progress.get("energy", 3),
        total_xp=progress.get("xp", 0),
        accuracy=accuracy,
        next_challenge=next_challenge,
        mastery_level=mastery_level,
    )


@app.route("/badges")
def badges():
    """Enhanced cosmic badges page"""
    progress = load_progress()
    stats = progress.get("stats", {})

    # Calculate badge statuses
    badges_data = {
        "earned_count": len(progress.get("badges", [])),
        "total_count": 15,  # Total available badges
        "first_lesson_complete": stats.get("total_questions", 0) >= 1,
        "knowledge_seeker": stats.get("correct_answers", 0) >= 25,
        "perfectionist": (
            stats.get("correct_answers", 0) / max(1, stats.get("total_questions", 1))
        )
        >= 0.9
        and stats.get("total_questions", 0) >= 20,
        "streak_champion": progress.get("streak", 0) >= 7,
        "aws_master": len(progress.get("badges", [])) >= 8,
        "guardian_protected": has_guardian_shield(progress),
        "correct_answers": stats.get("correct_answers", 0),
        "total_questions": stats.get("total_questions", 0),
        "current_accuracy": round(
            (stats.get("correct_answers", 0) / max(1, stats.get("total_questions", 1)))
            * 100
        ),
        "current_streak": progress.get("streak", 0),
        "domain_badges_earned": len(
            [b for b in progress.get("badges", []) if "Master" in b or "Architect" in b]
        ),
        # Dates (simplified)
        "first_lesson_date": date.today().isoformat(),
        "knowledge_seeker_date": date.today().isoformat(),
        "perfectionist_date": date.today().isoformat(),
        "streak_champion_date": date.today().isoformat(),
        "aws_master_date": date.today().isoformat(),
        "guardian_protected_date": date.today().isoformat(),
    }

    # AWS Domain badges (from your existing badges)
    aws_domain_badges = []
    existing_badges = progress.get("badges", [])

    domain_list = [
        {
            "name": "Monitoring Master",
            "icon": "📊",
            "description": "Master CloudWatch and monitoring",
        },
        {
            "name": "Security Sentinel",
            "icon": "🛡️",
            "description": "AWS security expert",
        },
        {
            "name": "DevOps Master",
            "icon": "🚀",
            "description": "CI/CD and automation guru",
        },
        {
            "name": "Database Architect",
            "icon": "🗄️",
            "description": "RDS and DynamoDB expert",
        },
        {
            "name": "Serverless Architect",
            "icon": "⚡",
            "description": "Lambda and serverless master",
        },
        {"name": "Container Master", "icon": "📦", "description": "ECS and EKS expert"},
    ]

    for domain in domain_list:
        aws_domain_badges.append(
            {
                "name": domain["name"],
                "icon": domain["icon"],
                "description": domain["description"],
                "earned": domain["name"] in existing_badges,
                "date": (
                    date.today().isoformat()
                    if domain["name"] in existing_badges
                    else None
                ),
                "hint": f"Complete {domain['name'].lower()} lessons with high accuracy",
            }
        )

    badges_data["completion_percentage"] = round(
        (badges_data["earned_count"] / badges_data["total_count"]) * 100
    )
    badges_data["aws_domain_badges"] = aws_domain_badges

    return render_template("badges_cosmic.html", **badges_data)


@app.route("/progress")
def progress_dashboard():
    """Duolingo + Slay the Spire inspired progress screen"""
    progress = load_progress()
    stats = progress.get("stats", {})
    platforms = get_platforms()

    # XP level: every 500 XP = 1 level
    total_xp = progress.get("xp", 0)
    level = max(1, total_xp // 500 + 1)
    level_xp = (level - 1) * 500
    next_level_xp = level * 500
    level_progress_pct = round(((total_xp - level_xp) / 500) * 100)

    # Accuracy
    total_q = stats.get("total_questions", 1)
    correct_q = stats.get("correct_answers", 0)
    accuracy = round((correct_q / total_q) * 100) if total_q > 0 else 0

    # Per-platform progress
    platform_stats = []
    for p in platforms:
        completed, total = get_platform_progress(progress, p["id"])
        pct = round((completed / total) * 100) if total > 0 else 0
        platform_stats.append({**p, "completed": completed, "total": total, "pct": pct})

    # Achievement definitions with unlock conditions
    all_achievements = [
        {
            "id": "first_victory",
            "name": "First Victory",
            "icon": "⚔️",
            "description": "Complete your first battle",
            "unlocked": "first_victory" in progress.get("achievements", []),
        },
        {
            "id": "elite_slayer",
            "name": "Elite Slayer",
            "icon": "👑",
            "description": "Defeat 3 elite challenges",
            "unlocked": "elite_slayer" in progress.get("achievements", []),
        },
        {
            "id": "boss_hunter",
            "name": "Boss Hunter",
            "icon": "🐉",
            "description": "Defeat your first boss",
            "unlocked": "boss_hunter" in progress.get("achievements", []),
        },
        {
            "id": "knowledge_seeker",
            "name": "Knowledge Seeker",
            "icon": "📚",
            "description": "Answer 100 questions",
            "unlocked": "knowledge_seeker" in progress.get("achievements", []),
        },
        {
            "id": "perfect_streak",
            "name": "Streak Champion",
            "icon": "🔥",
            "description": "Maintain a 7-day learning streak",
            "unlocked": "perfect_streak" in progress.get("achievements", []),
        },
        {
            "id": "aws_master",
            "name": "AWS Master",
            "icon": "☁️",
            "description": "Earn all domain badges",
            "unlocked": "aws_master" in progress.get("achievements", []),
        },
        {
            "id": "relic_collector",
            "name": "Relic Collector",
            "icon": "💎",
            "description": "Collect 5 different relics",
            "unlocked": "relic_collector" in progress.get("achievements", []),
        },
        {
            "id": "guardian_saved",
            "name": "Guardian's Chosen",
            "icon": "🛡️",
            "description": "Guardian's Shield saves you",
            "unlocked": "guardian_saved" in progress.get("achievements", []),
        },
    ]

    relics = progress.get("inventory", {}).get("relics", [])
    potions = progress.get("inventory", {}).get("potions", [])

    return render_template(
        "progress_dashboard.html",
        progress=progress,
        stats=stats,
        level=level,
        level_progress_pct=level_progress_pct,
        total_xp=total_xp,
        next_level_xp=next_level_xp,
        accuracy=accuracy,
        platform_stats=platform_stats,
        all_achievements=all_achievements,
        relics=relics,
        potions=potions,
    )


@app.route("/api/progress")
def api_progress():
    """API endpoint for raw progress data"""
    return jsonify(load_progress())


@app.route("/api/use-potion", methods=["POST"])
def use_potion():
    """Use a potion from inventory"""
    data = request.get_json()
    potion_name = data.get("potion")

    progress = load_progress()
    potions = progress.get("inventory", {}).get("potions", [])

    for i, potion in enumerate(potions):
        if potion.get("name") == potion_name:
            # Apply potion effect
            effect = ""
            if "Shield" in potion_name or "Health" in potion_name:
                progress["energy"] = progress.get("max_energy", 3)
                effect = "Energy shields fully restored!"
            elif "XP" in potion_name or "Boost" in potion_name:
                progress["xp"] += 25
                effect = "Gained 25 bonus XP!"

            # Remove used potion
            potions.pop(i)
            save_progress(progress)

            return jsonify({"success": True, "effect": effect})

    return jsonify({"success": False, "error": "Potion not found"})


# Helper functions
def get_recent_badges(progress):
    """Get recently earned badges"""
    badges = progress.get("badges", [])
    recent_badges = []

    # Get last 2 badges as "recent"
    for badge_name in badges[-2:]:
        recent_badges.append(
            {
                "name": badge_name,
                "description": f'Mastered {badge_name.lower().replace("master", "").replace("architect", "").strip()} concepts',
                "icon": get_badge_icon(badge_name),
            }
        )

    return recent_badges


def get_badge_icon(badge_name):
    """Get appropriate icon for badge"""
    if "Monitor" in badge_name:
        return "📊"
    elif "Security" in badge_name:
        return "🛡️"
    elif "DevOps" in badge_name or "Automation" in badge_name:
        return "🚀"
    elif "Database" in badge_name:
        return "🗄️"
    elif "Serverless" in badge_name:
        return "⚡"
    elif "Container" in badge_name:
        return "📦"
    elif "Network" in badge_name:
        return "🌐"
    elif "Cost" in badge_name:
        return "💰"
    else:
        return "🏆"


# ---------------------------------------------------------------------------
# Phase 1 API routes -- JSON endpoints for the Capacitor static shell
# ---------------------------------------------------------------------------


@app.route("/api/lessons")
def api_lessons():
    """Return all lessons as JSON."""
    return jsonify(get_lessons())


@app.route("/api/lesson/<int:lesson_id>")
def api_lesson(lesson_id):
    """Return a single lesson with current progress."""
    lessons = get_lessons()
    lesson = next((l for l in lessons if l["id"] == lesson_id), None)
    if not lesson:
        return jsonify({"error": "not found"}), 404
    progress = load_progress()
    return jsonify({"lesson": lesson, "progress": progress})


@app.route("/api/quiz/<int:lesson_id>", methods=["POST"])
def api_quiz(lesson_id):
    """Accept a quiz answer, return result and updated progress."""
    data = request.get_json(silent=True) or {}
    user_answer = data.get("answer")

    lessons = get_lessons()
    lesson = next((l for l in lessons if l["id"] == lesson_id), None)
    if not lesson:
        return jsonify({"error": "not found"}), 404

    if isinstance(lesson.get("answer"), list):
        correct = set(user_answer or []) == set(lesson["answer"])
    else:
        correct = user_answer == lesson.get("answer")

    progress, message, next_lesson_id = register_quiz_result(lesson_id, correct)
    return jsonify(
        {
            "correct": correct,
            "message": message,
            "next_lesson_id": next_lesson_id,
            "progress": progress,
            "explanation": lesson.get("explanation", ""),
        }
    )


@app.route("/api/platforms")
def api_platforms():
    """Return all platform data with progress."""
    progress = load_progress()
    platforms = get_platforms()
    result = []
    for p in platforms:
        completed, total = get_platform_progress(progress, p["id"])
        pct = round((completed / total) * 100) if total > 0 else 0
        result.append({**p, "completed": completed, "total": total, "pct": pct})
    return jsonify(result)


@app.route("/api/reward/<int:milestone_count>", methods=["POST"])
def api_reward(milestone_count):
    """Claim milestone reward, return bonus XP and updated progress."""
    progress = load_progress()
    bonus_xp = 50 + (milestone_count // 15) * 10
    progress["xp"] += bonus_xp
    save_progress(progress)
    return jsonify(
        {"bonus_xp": bonus_xp, "total_xp": progress["xp"], "progress": progress}
    )


if __name__ == "__main__":
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=5001, debug=debug)
