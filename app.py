from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
from improved_data import get_lessons
from progress import load_progress, complete_lesson, register_quiz_result
import random

# Cloud Orbit - Slay the Spire Edition v5
# Enhanced with room mechanics, loot system, and mobile APK preparation

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile app integration

@app.route('/')
def home():
    """
    Enhanced home page with Slay the Spire progression system
    """
    progress = load_progress()
    return render_template('index.html', progress=progress)

@app.route('/api/lessons')
def lessons_api():
    """API endpoint for mobile app integration"""
    return jsonify(get_lessons())

@app.route('/lessons')
def lessons():
    """Web version lessons list"""
    return jsonify(get_lessons())

@app.route('/lesson/<int:lesson_id>')
def lesson_page(lesson_id):
    """
    Enhanced lesson page with room mechanics
    """
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if lesson:
        progress = load_progress()
        return render_template('lesson.html', lesson=lesson, progress=progress)
    return "Lesson not found", 404

@app.route('/api/lesson/<int:lesson_id>')
def lesson_api(lesson_id):
    """API endpoint for lesson data (mobile)"""
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if lesson:
        progress = load_progress()
        return jsonify({
            'lesson': lesson,
            'progress': progress
        })
    return jsonify({'error': 'Lesson not found'}), 404

@app.route('/complete/<int:lesson_id>')
def complete(lesson_id):
    """
    Enhanced completion with loot rewards
    """
    progress = complete_lesson(lesson_id)
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)

    # Award loot if lesson has it
    if lesson and 'loot' in lesson:
        progress = award_loot(progress, lesson['loot'])

    next_id = lesson_id + 1 if lesson_id < len(lessons_list) else 1
    return redirect(url_for('lesson_page', lesson_id=next_id))

@app.route('/api/complete/<int:lesson_id>', methods=['POST'])
def complete_api(lesson_id):
    """API endpoint for lesson completion (mobile)"""
    progress = complete_lesson(lesson_id)
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)

    if lesson and 'loot' in lesson:
        progress = award_loot(progress, lesson['loot'])

    return jsonify({
        'success': True,
        'progress': progress,
        'loot_awarded': lesson.get('loot') if lesson else None
    })

@app.route('/quiz/<int:lesson_id>', methods=['GET', 'POST'])
def quiz(lesson_id):
    """
    Enhanced quiz with room battle mechanics
    """
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    
    if not lesson:
        return "Lesson not found", 404

    # ALWAYS load progress first - this is crucial
    progress = load_progress()

    if request.method == 'POST':
        # Handle single and multi-select questions
        if lesson.get('multi_select'):
            selected = request.form.getlist('option')
            correct_answers = set(lesson.get('answers', []))
            correct = set(selected) == correct_answers
        else:
            selected = request.form.get('option')
            correct = selected == lesson.get('answer')

        progress, message, next_lesson_id = register_quiz_result(lesson_id, correct)

        # Enhanced feedback based on room type and difficulty
        room_feedback = generate_room_feedback(lesson, correct)
        message += f"\n{room_feedback}"

        # Award loot on correct answers for elite/boss rooms
        if correct and lesson.get('room_type') in ['elite', 'boss'] and 'loot' in lesson:
            progress = award_loot(progress, lesson['loot'])
            message += f"\n🎁 You found loot: {lesson['loot']['name']}!"

        if progress['energy'] <= 0:
            return render_template('quiz.html', lesson=lesson, progress=progress,
                                   message=message + "\n⚡ Your shields are depleted! Rest at a campfire to recover.",
                                   repeat=True)
        elif correct:
            return render_template('quiz.html', lesson=lesson, progress=progress, message=message,
                                   repeat=False, next_lesson_id=next_lesson_id, correct=True)
        else:
            return render_template('quiz.html', lesson=lesson, progress=progress, message=message,
                                   repeat=True, correct=False)

    # GET request: show quiz form - ALWAYS include progress
    return render_template('quiz.html', lesson=lesson, progress=progress)

@app.route('/api/quiz/<int:lesson_id>', methods=['GET', 'POST'])
def quiz_api(lesson_id):
    """API endpoint for quiz interaction (mobile)"""
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if not lesson:
        return jsonify({'error': 'Lesson not found'}), 404

    if request.method == 'POST':
        data = request.get_json()
        selected = data.get('selected_answer')
        
        if lesson.get('multi_select'):
            correct_answers = set(lesson.get('answers', []))
            correct = set(selected) == correct_answers if isinstance(selected, list) else False
        else:
            correct = selected == lesson.get('answer')

        progress, message, next_lesson_id = register_quiz_result(lesson_id, correct)
        room_feedback = generate_room_feedback(lesson, correct)
        
        loot_awarded = None
        if correct and lesson.get('room_type') in ['elite', 'boss'] and 'loot' in lesson:
            progress = award_loot(progress, lesson['loot'])
            loot_awarded = lesson['loot']

        return jsonify({
            'correct': correct,
            'progress': progress,
            'message': message,
            'room_feedback': room_feedback,
            'next_lesson_id': next_lesson_id,
            'loot_awarded': loot_awarded,
            'explanation': lesson.get('explanation', '')
        })

    # GET request
    progress = load_progress()
    return jsonify({
        'lesson': lesson,
        'progress': progress
    })

@app.route('/api/progress')
def progress_api():
    """API endpoint for progress data (mobile)"""
    return jsonify(load_progress())

@app.route('/api/map')
def adventure_map():
    """
    Generate Slay the Spire style adventure map
    """
    lessons = get_lessons()
    progress = load_progress()

    # Create map nodes with connections
    map_data = {
        'nodes': [],
        'current_position': progress.get('current_lesson', 1),
        'completed_lessons': progress.get('completed_lessons', [])
    }

    for lesson in lessons:
        node = {
            'id': lesson['id'],
            'title': lesson['title'],
            'room_type': lesson.get('room_type', 'battle'),
            'difficulty': lesson.get('difficulty', 'easy'),
            'completed': lesson['id'] in progress.get('completed_lessons', []),
            'available': lesson['id'] <= progress.get('current_lesson', 1),
            'connections': get_node_connections(lesson['id'], len(lessons))
        }
        map_data['nodes'].append(node)

    return jsonify(map_data)

def generate_room_feedback(lesson, correct):
    """Generate contextual feedback based on room type and result"""
    room_type = lesson.get('room_type', 'battle')
    difficulty = lesson.get('difficulty', 'easy')
    
    if correct:
        feedback_options = {
            'battle': ["💥 Victory! You've mastered this concept!", "⚔️ Combat successful! Knowledge gained!"],
            'elite': ["👑 Elite defeated! You've proven your expertise!", "🏆 Masterful performance against this challenge!"],
            'boss': ["🐉 BOSS DEFEATED! You are a true AWS champion!", "👑 Legendary victory! You've conquered the ultimate test!"],
            'shop': ["💰 Wise purchase! This knowledge will serve you well!", "🛒 Excellent choice! Your understanding grows!"],
            'event': ["✨ Fortunate outcome! Your intuition guides you well!", "🎲 Lucky choice! Fortune favors the prepared!"]
        }
    else:
        feedback_options = {
            'battle': ["💔 Defeated... but you learn from every battle!", "⚔️ This foe bests you today, but you'll return stronger!"],
            'elite': ["😵 Elite victory... their power was too great!", "👹 The elite's knowledge exceeds yours... for now!"],
            'boss': ["💀 The boss remains undefeated... more preparation needed!", "🐲 This ancient knowledge still eludes you!"],
            'shop': ["💸 Perhaps not the right choice... consider carefully!", "🤔 Maybe reconsider this investment!"],
            'event': ["😓 Unfortunate outcome... but wisdom comes from experience!", "🎲 Lady Luck was not with you this time!"]
        }

    return random.choice(feedback_options.get(room_type, feedback_options['battle']))

def award_loot(progress, loot):
    """Award loot to player inventory"""
    if 'inventory' not in progress:
        progress['inventory'] = {'relics': [], 'potions': [], 'gold': 0}

    loot_type = loot.get('type', 'knowledge_card')
    
    if loot_type == 'relic':
        progress['inventory']['relics'].append(loot)
    elif loot_type == 'potion':
        progress['inventory']['potions'].append(loot)
    elif loot_type == 'gold':
        progress['inventory']['gold'] += loot.get('amount', 50)
    elif loot_type == 'legendary_relic':
        progress['inventory']['relics'].append(loot)
        progress['xp'] += 100  # Bonus XP for legendary items

    # Save progress with new loot
    from progress import save_progress
    save_progress(progress)
    return progress

def get_node_connections(node_id, total_nodes):
    """Generate connections for map nodes (simplified linear progression)"""
    connections = []
    if node_id < total_nodes:
        connections.append(node_id + 1)
    return connections

# Health check endpoint for deployment
@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'version': '5.0'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)