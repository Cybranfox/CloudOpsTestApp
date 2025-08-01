from flask import Flask, render_template, request, redirect, url_for
from src.adventure_mode.map import get_act1_map
from src.adventure_mode import questions
from src.rpg_engine.player import Player
from src.rpg_engine.combat import handle_answer
from src.exam_simulator.exam import Exam

app = Flask(__name__)

# In-memory player session (no persistence for prototype)
player = Player()
exam_session = None

@app.route('/')
def main_menu():
    return render_template('main_menu.html', player=player)

@app.route('/adventure')
def adventure():
    # load act 1 map for demonstration
    game_map = get_act1_map()
    return render_template('adventure.html', game_map=game_map, player=player)

@app.route('/battle/<node_id>', methods=['GET', 'POST'])
def battle(node_id):
    node = next((n for n in get_act1_map() if n['id'] == node_id), None)
    if not node:
        return "Invalid node", 404
    # Dynamically select a question based on node id.  If the node defines
    # its own question it will be used, otherwise we pull from the question
    # bank to provide variety on each playthrough.
    question = None
    explanation = None
    if node_id == 'ec2_battle':
        q = questions.get_random_ec2_question()
        # shuffle options for variety
        opts = q['options'][:]
        import random
        random.shuffle(opts)
        question = {"prompt": q['prompt'], "options": opts, "answer": q['answer']}
        explanation = q['explanation']
    elif node_id == 's3_challenge':
        q = questions.get_random_s3_question()
        opts = q['options'][:]
        import random
        random.shuffle(opts)
        question = {"prompt": q['prompt'], "options": opts, "answer": q['answer']}
        explanation = q['explanation']
    elif node_id == 'auto_scaling_boss':
        q = questions.get_random_autoscaling_question()
        opts = q['options'][:]
        import random
        random.shuffle(opts)
        question = {"prompt": q['prompt'], "options": opts, "answer": q['answer']}
        explanation = q['explanation']
    elif node_id == 'lifecycle_boss':
        q = questions.get_random_lifecycle_question()
        opts = q['options'][:]
        import random
        random.shuffle(opts)
        question = {"prompt": q['prompt'], "options": opts, "answer": q['answer']}
        explanation = q['explanation']
    else:
        # Use predefined question if available
        question = node.get('question')
        explanation = node.get('explanation')
    if request.method == 'POST':
        answer = request.form.get('answer')
        # Evaluate answer; handle_answer returns 'correct' or 'wrong'
        result = handle_answer(player, question, answer)
        return render_template('battle_result.html', result=result, explanation=explanation, player=player)
    return render_template('battle.html', question=question, node=node, player=player)

@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/exams', methods=['GET', 'POST'])
def exams():
    global exam_session
    if request.method == 'POST':
        # Start exam
        exam_session = Exam()
        return redirect(url_for('exam_take'))
    return render_template('exams.html', exam_session=exam_session)

@app.route('/exam')
def exam_take():
    global exam_session
    if not exam_session:
        return redirect(url_for('exams'))
    if exam_session.is_finished():
        # Evaluate results
        return render_template('exam_result.html', score=exam_session.score(), player=player)
    # Present next question
    q = exam_session.next_question()
    return render_template('exam_question.html', question=q, time_left=exam_session.time_left())

@app.route('/exam/answer', methods=['POST'])
def exam_answer():
    global exam_session
    if not exam_session:
        return redirect(url_for('exams'))
    answer = request.form.get('answer')
    exam_session.submit_answer(answer)
    return redirect(url_for('exam_take'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
