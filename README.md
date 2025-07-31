# CloudOps Test App

This is a simple Flask application to help you get started with deploying and running an application on AWS or your local machine.

## Prerequisites

- Python 3.8 or later installed on your machine
- `pip` package installer (usually comes with Python)

## Setup

1. Create a virtual environment (recommended) and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Open your browser and go to `http://localhost:5000`. You should see the message:

> Welcome to your CloudOps Test App!

## Notes

- You can start modifying `app.py` to add new routes and functionality.
- Remember to deactivate your virtual environment when you're done: `deactivate`.
