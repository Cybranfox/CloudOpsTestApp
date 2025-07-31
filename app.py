from flask import Flask, render_template, jsonify, request, redirect, url_for
from data import get_lessons
from progress import load_progress, complete_lesson, register_quiz_result

#
# AWS Orbit App v4
#
# This version expands on the initial prototype by adding a simple gamification layer:
#
#  * Energy shields: Users start with three shields. Each incorrect quiz answer
#    deducts one shield. When all shields are depleted the user is prompted
#    to review material before continuing. Completing a lesson or answering
#    correctly restores one shield (up to the max).
#  * Badges: After completing all lessons, the user earns a badge named for
#    the domain (e.g. "Monitoring Master"). Badges are displayed on the
#    homepage. Additional badges can be added in data.py.
#  * Adaptive navigation: Quiz results influence navigation—correct answers
#    advance to the next lesson, incorrect answers repeat the current lesson.
#
app = Flask(__name__)


@app.route('/')
def home():
    """
    Home page displaying user progress: XP, streak, energy shields and badges.
    """
    progress = load_progress()
    return render_template('index.html', progress=progress)


@app.route('/lessons')
def lessons():
    return jsonify(get_lessons())


@app.route('/lesson/<int:lesson_id>')
def lesson_page(lesson_id):
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if lesson:
        return render_template('lesson.html', lesson=lesson)
    return "Lesson not found", 404


@app.route('/complete/<int:lesson_id>')
def complete(lesson_id):
    """
    Mark a lesson as completed (awards XP and restores a shield) and
    redirect to the next lesson or home if finished.
    """
    progress = complete_lesson()
    lessons_list = get_lessons()
    next_id = lesson_id + 1 if lesson_id < len(lessons_list) else 1
    return redirect(url_for('lesson_page', lesson_id=next_id))


@app.route('/quiz/<int:lesson_id>', methods=['GET', 'POST'])
def quiz(lesson_id):
    """
    Display a quiz for the given lesson. On POST, evaluate the answer and
    update progress: correct answers award XP and restore a shield; incorrect
    answers deduct a shield. If the user runs out of shields they must
    revisit the lesson before continuing.
    """
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if not lesson:
        return "Lesson not found", 404
    if request.method == 'POST':
        # Handle single and multi‑select questions
        if lesson.get('multi_select'):
            selected = request.form.getlist('option')  # list of selected options
            correct_answers = set(lesson.get('answers', []))
            correct = set(selected) == correct_answers
        else:
            selected = request.form.get('option')
            correct = selected == lesson.get('answer')
        progress, message, next_lesson_id = register_quiz_result(lesson_id, correct)
        if progress['energy'] <= 0:
            # When energy depleted, prompt to review the current lesson
            return render_template('quiz.html', lesson=lesson, message=message + "\nYou have lost all your shields! Please review the lesson before trying again.", repeat=True)
        elif correct:
            # Redirect to next lesson's lesson page
            return redirect(url_for('lesson_page', lesson_id=next_lesson_id))
        else:
            # incorrect answer but shields remain: repeat quiz
            return render_template('quiz.html', lesson=lesson, message=message, repeat=True)
    # GET request
    # GET request: show quiz form and current progress (energy)
    from progress import load_progress
    prog = load_progress()
    return render_template('quiz.html', lesson=lesson, progress=prog)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)