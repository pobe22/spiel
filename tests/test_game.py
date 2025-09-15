import unittest
from core.game import QuizGame
from data import questions_dtsm

class TestQuizGame(unittest.TestCase):
    def setUp(self):
        self.game = QuizGame(questions_dtsm.questions2ADAC_DTSM)

    def test_question_count(self):
        self.assertGreater(len(self.game.questions), 0)

    def test_check_answer_correct(self):
        question, options = self.game.get_next_question()
        correct_option = options['correct']
        result = self.game.check_answer(question, correct_option)
        self.assertTrue(result)

    def test_check_answer_incorrect(self):
        question, options = self.game.get_next_question()
        wrong_option = 'a' if options['correct'] != 'a' else 'b'
        result = self.game.check_answer(question, wrong_option)
        self.assertFalse(result)
        self.assertIn((question, options), self.game.asked_questions)

if __name__ == "__main__":
    unittest.main()
