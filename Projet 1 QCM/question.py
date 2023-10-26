import random


class Question:
    def __init__(self, intitule, reponses):
        self.intitule = intitule
        self.reponses = reponses
        random.shuffle(self.reponses)
