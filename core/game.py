import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class QuizGame:
    def __init__(self, question_set):
        # Prüfen, ob dict oder list übergeben wurde
        if isinstance(question_set, dict):
            # dict: items() behalten
            self.questions = list(question_set.items())
        elif isinstance(question_set, list):
            # list: direkt übernehmen
            self.questions = question_set.copy()
        else:
            raise TypeError("question_set muss dict oder list von Fragen sein")

        random.shuffle(self.questions)
        self.current_index = 0
        self.asked_questions = []

    def has_next(self):
        return self.current_index < len(self.questions)

    def get_next_question(self):
        if self.has_next():
            # Unterscheiden, ob dict (Liste) oder tuple (dict von dicts)
            q = self.questions[self.current_index]
            self.current_index += 1
            if isinstance(q, tuple):
                # dict von dicts
                question, options = q
                return question, options
            else:
                # Liste von Fragen
                return q
        return None

    def check_answer(self, question, selected_option):
        # Wenn tuple (dict von dicts)
        if isinstance(question, tuple):
            options = dict(question[1])
            correct = options['correct']
            question_text = question[0]
        else:
            # Liste von Fragen
            options = dict(question)
            correct = options['correct']
            question_text = options['question']

        if selected_option.lower() == correct.lower():
            return True
        else:
            self.asked_questions.append(question)
            return False

    def reset_wrong_questions(self):
        self.questions = self.asked_questions[:]
        random.shuffle(self.questions)
        self.current_index = 0
        self.asked_questions = []
