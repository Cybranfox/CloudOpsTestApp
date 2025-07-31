from flask import Flask, render_template, jsonify
from data import get_lessons

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    # Return list of lessons as JSON
    return jsonify(get_lessons())

@app.route('/lesson/<int:lesson_id>')
def lesson_page(lesson_id):
    # Find lesson by ID
    lessons_list = get_lessons()
    lesson = next((l for l in lessons_list if l['id'] == lesson_id), None)
    if lesson:
        return render_template('lesson.html', lesson=lesson)
    return "Lesson not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
