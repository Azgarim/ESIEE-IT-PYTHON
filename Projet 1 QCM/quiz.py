class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.historique = []

    def poser_question(self, question):
        print(question.intitule)

        # Affichage des réponses possibles
        for i, reponse in enumerate(question.reponses):
            lettre = chr(97 + i)  # Convertit 0, 1, 2 en 'a', 'b', 'c' respectivement
            print(f"{lettre}. {reponse.texte}")

        # Obtention de la réponse de l'utilisateur
        reponse_utilisateur = input("Votre réponse (a, b ou c): ").lower()

        # Vérification de la validité de l'input
        while reponse_utilisateur not in ['a', 'b', 'c']:
            print("Erreur : veuillez entrer 'a', 'b' ou 'c'.")
            reponse_utilisateur = input("Votre réponse (a, b ou c): ").lower()

        # Vérification de la réponse
        index = ord(reponse_utilisateur) - 97
        est_correcte = question.reponses[index].est_correcte
        if est_correcte:
            self.score += 1

        # Enregistrement des détails pour le récapitulatif
        correcte = [reponse.texte for reponse in question.reponses if reponse.est_correcte][0]
        self.historique.append({
            "question": question.intitule,
            "reponse_choisie": question.reponses[index].texte,
            "est_correcte": est_correcte,
            "bonne_reponse": correcte
        })

    def commencer(self):
        for question in self.questions:
            self.poser_question(question)

        # Afficher le score
        print(f"Votre score est de {self.score}/{len(self.questions)}")

        # Afficher le récapitulatif
        print("\nRécapitulatif du quiz:")
        for entry in self.historique:
            est_correcte = "Correct" if entry["est_correcte"] else "Incorrect"
            print(f"Question: {entry['question']}\nVotre réponse: {entry['reponse_choisie']} ({est_correcte})\nBonne réponse: {entry['bonne_reponse']}\n")
