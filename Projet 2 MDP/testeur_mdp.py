import math


class TesteurMDP:
    # Constructeur de la classe, initialisé avec un mot de passe donné
    def __init__(self, mdp=""):
        self.mdp = mdp

    # Méthode pour calculer l'entropie du mot de passe
    def calculer_entropie(self):
        longueur = len(self.mdp)

        # Définition des différents ensembles de caractères
        min_chars = 'abcdefghijklmnopqrstuvwxyz'
        maj_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num_chars = '0123456789'
        special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'

        # Calcul de la taille de l'alphabet utilisé dans le mot de passe
        taille_alphabet = 0
        if any(c in min_chars for c in self.mdp):
            taille_alphabet += len(min_chars)
        if any(c in maj_chars for c in self.mdp):
            taille_alphabet += len(maj_chars)
        if any(c in num_chars for c in self.mdp):
            taille_alphabet += len(num_chars)
        if any(c in special_chars for c in self.mdp):
            taille_alphabet += len(special_chars)

        # Calcul de l'entropie en se basant sur la formule de l'entropie
        return longueur * math.log2(taille_alphabet)

    # Méthode pour évaluer la force du mot de passe en fonction de son entropie
    def evaluer_force(self):
        entropie = self.calculer_entropie()
        # Catégorisation de l'entropie
        if entropie < 64:
            return "très faible"
        elif 64 <= entropie < 80:
            return "faible"
        elif 80 <= entropie < 100:
            return "moyen"
        else:
            return "fort"

    # Méthode combinée pour évaluer à la fois l'entropie et la force du mot de passe
    def evaluer(self):
        entropie = self.calculer_entropie()
        force = self.evaluer_force()
        return entropie, force
