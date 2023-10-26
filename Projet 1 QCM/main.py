import random
from question import Question
from reponse import Reponse
from quiz import Quiz
from jeu_questions import jeu_predefini


# Création des questions et des réponses. Questions trouvées sur https://www.etudier.com/dissertations/100-Questions-De-Culture-G%C3%A9n%C3%A9rale/47163.html car je n'ai aucune imagination
questions = [
    Question("Quelle pièce est absolument à protéger dans un jeu d’échec ?", [
        Reponse("La reine", False),
        Reponse("Le pion", False),
        Reponse("Le roi", True)
    ]),
    Question("Quel est la capitale de l’Australie ?", [
        Reponse("Sydney", False),
        Reponse("Melbourne", False),
        Reponse("Canberra", True)
    ]),
    Question("Qui sont les animateurs du festival « juste pour rire » ?", [
        Reponse("Éric et Ramzy", False),
        Reponse("Stéphane rousseau et Franck Dubosc", True),
        Reponse("Kad et Olivier", False)
    ]),
    Question("Qui anime Secret Story?", [
        Reponse("Nikos Aliagas", False),
        Reponse("Cyril Hanouna", False),
        Reponse("Benjamin Castaldi", True)
    ]),
    Question("A combien, d’exemplaire, à 10000 près s’est vendu pour toi public 2?", [
        Reponse("350 000", False),
        Reponse("550 000", False),
        Reponse("450 000", True)
    ]),
    Question("Combien de nouvelles chaînes sont apparues grâce à la TNT ?", [
        Reponse("8", False),
        Reponse("16", False),
        Reponse("12", True)
    ]),
    Question("Quel est la phrase fétiche de Chevalier et Laspalès ?", [
        Reponse("À la vôtre!", False),
        Reponse("C'est vous qui voyez", True),
        Reponse("Jamais sans ma pipe", False)
    ]),
    Question("Combien y a-t-il de signes astrologiques chinois ?", [
        Reponse("10", False),
        Reponse("14", False),
        Reponse("12", True)
    ]),
    Question("Quel est le 2ème nom de l’hippocampe ?", [
        Reponse("Le poisson-cavalier", False),
        Reponse("Le cheval marin", False),
        Reponse("Le cheval de mer", True)
    ]),
    Question("En quelle année est mort JFK ?", [
        Reponse("1961", False),
        Reponse("1965", False),
        Reponse("1963", True)
    ]),
    Question("Combien de dieux trônent à l'Olympe ?", [
        Reponse("10", False),
        Reponse("14", False),
        Reponse("12", True)
    ]),
    Question("Qu'appelle-t-on la canopée ?", [
        Reponse("La base de la forêt amazonienne", False),
        Reponse("Le sommet de la forêt amazonienne", True),
        Reponse("Le milieu de la forêt amazonienne", False)
    ]),
    Question("Quel est le dernier album de Britney Spears ?", [
        Reponse("Femme Fatale", False),
        Reponse("Blackout", False),
        Reponse("Circus", True)
    ]),
    Question("Quel est l'équivalent du pape au Tibet ?", [
        Reponse("Le moine supérieur", False),
        Reponse("Le prêtre principal", False),
        Reponse("Le dalai lama", True)
    ]),
    Question("Quelle est la différence entre le chameau et le dromadaire ?", [
        Reponse("La taille", False),
        Reponse("Le lieu de vie", False),
        Reponse("Le nombre de bosses", True)
    ]),
    Question("Quel précipité observe-t-on quand on mélange du nitrate d'argent avec du chlore ?", [
        Reponse("Un précipité rouge", False),
        Reponse("Un précipité jaune", False),
        Reponse("Un précipité blanc qui se noircit", True)
    ]),
    Question("Quelle est la voiture dans Retour vers le futur ?", [
        Reponse("Ford Mustang", False),
        Reponse("Doloréanne", True),
        Reponse("Chevrolet Impala", False)
    ]),
    Question("Qui est le réalisateur du film « camping » ?", [
        Reponse("D.Boon", False),
        Reponse("G.Lellouche", False),
        Reponse("R.Antonniente", True)
    ]),
    Question("Comment s'appelle l'équivalent du musée Grévin à Londres ?", [
        Reponse("Royal Wax Museum", False),
        Reponse("London Figures", False),
        Reponse("Madame Tussaud", True)
    ])
]

questions2 = jeu_predefini()

for q in questions:
    bonnes_reponses = [r for r in q.reponses if r.est_correcte]

    if len(bonnes_reponses) != 1:
        raise ValueError(
            f"La question '{q.intitule}' a {len(bonnes_reponses)} bonnes réponses. Il devrait y en avoir exactement une.")

# Mélange aléatoire de la liste des questions
random.shuffle(questions2)
questions_melangees = random.sample(questions, 10)

# Création du quiz et démarrage du quiz
quiz = Quiz(questions2[:10])
quiz.commencer()
