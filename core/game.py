import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class QuizGame:
    def __init__(self, question_set):
        self.questions = list(question_set.items())
        random.shuffle(self.questions)
        self.current_index = 0
        self.asked_questions = []

    def has_next(self):
        return self.current_index < len(self.questions)

    def get_next_question(self):
        if self.has_next():
            question, options = self.questions[self.current_index]
            self.current_index += 1
            return question, options
        return None, None

    def check_answer(self, question, selected_option):
        options = dict(self.questions[self.current_index - 1][1])
        correct = options['correct']
        if selected_option.lower() == correct.lower():
            return True
        else:
            self.asked_questions.append((question, options))
            return False

    def reset_wrong_questions(self):
        self.questions = self.asked_questions[:]
        random.shuffle(self.questions)
        self.current_index = 0
        self.asked_questions = []
