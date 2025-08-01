import time
class Exam:
    def __init__(self):
        self.start_time = time.time()
        self.questions = [
            {"prompt": "Which service monitors metrics and logs?", "options": ["CloudTrail", "CloudWatch", "IAM", "EC2"], "answer": "CloudWatch"},
            {"prompt": "What is the default VPC CIDR block size?", "options": ["/16", "/20", "/24", "/28"], "answer": "/16"},
        ]
        self.current_index = 0
        self.correct_count = 0
        self.duration = 130 * 60  # 130 minutes

    def next_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def submit_answer(self, answer):
        q = self.questions[self.current_index]
        if answer == q['answer']:
            self.correct_count += 1
        self.current_index += 1

    def is_finished(self):
        return self.current_index >= len(self.questions) or self.time_left() <= 0

    def time_left(self):
        elapsed = time.time() - self.start_time
        return max(0, self.duration - elapsed)

    def score(self):
        return int((self.correct_count / len(self.questions)) * 100)
