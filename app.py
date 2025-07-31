from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to your CloudOps Test App!'

if __name__ == '__main__':
    # When running locally, enable debug mode for automatic reloads
    app.run(host='0.0.0.0', port=5000, debug=True)
