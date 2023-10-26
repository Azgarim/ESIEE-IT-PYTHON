import unittest
from quiz import Quiz
from question import Question
from reponse import Reponse
class TestQuiz(unittest.TestCase):

    def setUp(self):
        # On créé une fausse liste de questions pour le test
        self.questions = [
            Question("Question test 1 ?", [
                Reponse("Réponse A", False),
                Reponse("Réponse B", True),
                Reponse("Réponse C", False)
            ]),
            Question("Question test 2 ?", [
                Reponse("Réponse A", False),
                Reponse("Réponse B", False),
                Reponse("Réponse C", True)
            ])
        ]
        self.quiz = Quiz(self.questions)

    def test_initialisation(self):
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(len(self.quiz.historique), 0)

    def test_historique(self):
        # On simule des réponses à ajouter à l'historique
        self.quiz.historique.append({"question": "Question test 1 ?", "reponse_choisie": "Réponse B", "est_correcte": True})
        self.quiz.historique.append({"question": "Question test 2 ?", "reponse_choisie": "Réponse C", "est_correcte": True})

        self.assertEqual(len(self.quiz.historique), 2)
        self.assertEqual(self.quiz.historique[0]['est_correcte'], True)
        self.assertEqual(self.quiz.historique[1]['est_correcte'], True)

if __name__ == "__main__":
    unittest.main()
