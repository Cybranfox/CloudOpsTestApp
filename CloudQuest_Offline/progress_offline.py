"""
Offline-optimized progress tracking
Ensures all data is saved locally without any network dependencies
"""
import json
import os
from datetime import datetime, date

PROGRESS_FILE = 'progress_offline.json'

def load_progress():
    """Load progress from local file"""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    
    # Default offline progress
    return {
        'current_lesson': 1,
        'xp': 0,
        'energy': 3,
        'max_energy': 3,
        'streak': 0,
        'last_active': str(date.today()),
        'completed_lessons': [],
        'badges': [],
        'stats': {
            'total_questions': 0,
            'correct_answers': 0,
            'total_time': 0
        },
        'inventory': {
            'relics': [],
            'potions': []
        },
        'offline_mode': True
    }

def save_progress(progress):
    """Save progress to local file"""
    progress['last_saved'] = datetime.now().isoformat()
    progress['offline_mode'] = True
    
    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f, indent=2)
        return True
    except Exception as e:
        print(f"Warning: Could not save progress: {e}")
        return False

# Export the same interface as the original
def register_quiz_result(lesson_id, correct):
    """Register quiz result offline"""
    progress = load_progress()
    
    # Update stats
    progress['stats']['total_questions'] += 1
    if correct:
        progress['stats']['correct_answers'] += 1
        progress['xp'] += 10
        if progress['energy'] < progress['max_energy']:
            progress['energy'] += 1
    else:
        progress['energy'] = max(0, progress['energy'] - 1)
    
    # Update lesson completion
    if correct and lesson_id not in progress['completed_lessons']:
        progress['completed_lessons'].append(lesson_id)
        progress['current_lesson'] = max(progress['current_lesson'], lesson_id + 1)
    
    save_progress(progress)
    
    message = "Correct! +10 XP" if correct else "Try again!"
    next_lesson = lesson_id + 1 if correct else lesson_id
    
    return progress, message, next_lesson

def complete_lesson(lesson_id):
    """Mark lesson as complete"""
    progress = load_progress()
    if lesson_id not in progress['completed_lessons']:
        progress['completed_lessons'].append(lesson_id)
        progress['current_lesson'] = max(progress['current_lesson'], lesson_id + 1)
    save_progress(progress)
    return progress

def check_achievements(progress):
    """Check for new achievements"""
    new_badges = []
    
    stats = progress.get('stats', {})
    correct = stats.get('correct_answers', 0)
    total = stats.get('total_questions', 0)
    
    # Achievement logic
    if correct >= 10 and 'Quick Learner' not in progress['badges']:
        new_badges.append('Quick Learner')
    
    if total >= 50 and 'Dedicated Student' not in progress['badges']:
        new_badges.append('Dedicated Student')
    
    if correct >= 100 and 'AWS Expert' not in progress['badges']:
        new_badges.append('AWS Expert')
    
    # Add new badges
    progress['badges'].extend(new_badges)
    save_progress(progress)
    
    return new_badges

def has_guardian_shield(progress):
    """Check if guardian shield is active"""
    return 'Guardian Shield' in progress.get('badges', [])
