import json
import os
from datetime import date
from data import get_lessons


# Path to progress file within this directory
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), 'progress.json')

# Default progress structure
DEFAULT_PROGRESS = {
    "xp": 0,
    "streak": 0,
    "last_completed_date": None,
    "energy": 3,  # number of energy shields available
    "badges": [],  # list of earned badge names
    "completed_lessons": []  # lesson IDs completed successfully
}


def _init_progress_file():
    """
    Create the progress file if it does not exist.
    """
    if not os.path.isfile(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(DEFAULT_PROGRESS, f)


def load_progress():
    """
    Load the user's progress from disk. If the file does not exist
    initialise it with default values.
    """
    _init_progress_file()
    with open(PROGRESS_FILE, 'r') as f:
        return json.load(f)


def save_progress(progress):
    """
    Persist the progress dictionary to disk.
    """
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)


def complete_lesson(xp_gain=10):
    """
    Mark a lesson as completed. This function awards XP, manages the daily
    streak and restores one energy shield (up to the maximum of 3). It does
    not track which lesson was completed; that is handled by register_quiz_result.

    Args:
        xp_gain (int): Amount of XP to award.

    Returns:
        dict: Updated progress.
    """
    progress = load_progress()
    today = date.today().isoformat()
    if progress.get('last_completed_date') == today:
        progress['streak'] += 1
    else:
        progress['streak'] = 1
    progress['last_completed_date'] = today
    progress['xp'] += xp_gain
    # Restore one shield when completing a lesson (capped at 3)
    progress['energy'] = min(3, progress.get('energy', 3) + 1)
    save_progress(progress)
    return progress


def register_quiz_result(lesson_id, correct, xp_gain_correct=20, xp_gain_incorrect=0):
    """
    Update progress based on quiz outcome. When the answer is correct it awards
    XP, restores one energy shield (up to 3) and marks the lesson as completed,
    potentially unlocking a badge. Incorrect answers deduct one shield. If
    energy reaches zero the caller should prompt the user to review the
    material.

    Args:
        lesson_id (int): ID of the lesson being quizzed.
        correct (bool): Whether the user's answer was correct.
        xp_gain_correct (int): XP to award for a correct answer.
        xp_gain_incorrect (int): XP to award for an incorrect answer (defaults to 0).

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
    if correct:
        # Award XP
        progress['xp'] += xp_gain_correct
        # Restore one shield up to max
        progress['energy'] = min(3, progress.get('energy', 3) + 1)
        # Build base success message and append the lesson explanation so the
        # mascot can elaborate on the concept for the user. Including the
        # explanation here ensures it travels back to the client and can be
        # displayed alongside the celebration animation.
        message = f"Correct! You've earned {xp_gain_correct} XP."
        if lesson.get('explanation'):
            message += f"\nExplanation: {lesson['explanation']}"
        # Record completion if not already done
        if lesson_id not in progress.get('completed_lessons', []):
            progress['completed_lessons'].append(lesson_id)
            # Award badge for this lesson
            badge_name = lesson.get('badge')
            if badge_name and badge_name not in progress.get('badges', []):
                progress['badges'].append(badge_name)
                message += f" You earned the {badge_name} badge!"
        # Determine next lesson ID: if at end go back to first
        next_lesson_id = lesson_id + 1 if lesson_id < len(lessons) else 1
    else:
        # Deduct a shield
        progress['energy'] = progress.get('energy', 3) - 1
        message = "Incorrect answer. You lose one shield."
        # Award minimal XP for participation
        progress['xp'] += xp_gain_incorrect
        # Keep the same lesson to allow retry
        next_lesson_id = lesson_id
    save_progress(progress)
    return progress, message, next_lesson_id