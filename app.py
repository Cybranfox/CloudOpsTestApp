from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lesson')
def lesson():
    # Dummy lesson content; replace with actual content later
    return {
        "title": "Monitoring, Logging & Remediation",
        "content": "In this lesson, you'll learn how to configure CloudWatch metrics, alarms and use CloudTrail logs for monitoring AWS workloads."
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
