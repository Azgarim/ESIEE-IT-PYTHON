from question import Question
from reponse import Reponse

def jeu_predefini():
    return [
        Question("Quelle est la plus grande planète du système solaire ?", [
            Reponse("Mars"),
            Reponse("Jupiter", est_correcte=True),
            Reponse("Vénus")
        ]),
        Question("Quelle langue est parlée au Brésil ?", [
            Reponse("Espagnol"),
            Reponse("Anglais"),
            Reponse("Portugais", est_correcte=True)
        ]),
        Question("Qui a écrit 'Le Petit Prince' ?", [
            Reponse("Victor Hugo"),
            Reponse("Antoine de Saint-Exupéry", est_correcte=True),
            Reponse("Albert Camus")
        ]),
        Question("Quel pays est le plus peuplé du monde ?", [
            Reponse("Inde"),
            Reponse("États-Unis"),
            Reponse("Chine", est_correcte=True)
        ]),
        Question("Quel instrument a trois cordes ?", [
            Reponse("Balalaïka", est_correcte=True),
            Reponse("Guitare"),
            Reponse("Violon")
        ]),
        Question("Quelle molécule est responsable de la génétique ?", [
            Reponse("Protéine"),
            Reponse("ADN", est_correcte=True),
            Reponse("Glucide")
        ]),
        Question("Combien de dents a un adulte en incluant les dents de sagesse ?", [
            Reponse("32", est_correcte=True),
            Reponse("28"),
            Reponse("30")
        ]),
        Question("Quelle est la capitale de la Suède ?", [
            Reponse("Oslo"),
            Reponse("Stockholm", est_correcte=True),
            Reponse("Copenhague")
        ]),
        Question("De quel jeu vidéo provient le personnage de Mario ?", [
            Reponse("Tetris"),
            Reponse("Sonic"),
            Reponse("Super Mario", est_correcte=True)
        ]),
        Question("Quelle est la couleur obtenue en mélangeant du bleu et du jaune ?", [
            Reponse("Vert", est_correcte=True),
            Reponse("Orange"),
            Reponse("Violet")
        ])
    ]
