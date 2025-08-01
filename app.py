from flask import Flask, jsonify, request, render_template
from src.rpg.skill_tree import get_skill_tree
from src.rpg.minigames.security_dungeon import evaluate_security_dungeon
from src.adaptive_learning.engine import next_content

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/skill_tree')
def skill_tree():
    return jsonify(get_skill_tree())

@app.route('/api/minigame/security_dungeon', methods=['POST'])
def security_dungeon():
    data = request.get_json()
    policy = data.get('policy', '')
    result = evaluate_security_dungeon(policy)
    return jsonify(result)

@app.route('/api/next_content', methods=['POST'])
def get_next_content():
    user = request.get_json()
    return jsonify(next_content(user))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
