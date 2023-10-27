import random

class GenerateurMDP:
    # Constructeur de la classe, initialisé avec le nombre de différents types de caractères souhaités pour le mot de passe
    def __init__(self, minuscules=0, majuscules=0, chiffres=0, speciaux=0):
        self.minuscules = minuscules  # Nombre de caractères minuscules désiré
        self.majuscules = majuscules  # Nombre de caractères majuscules désiré
        self.chiffres = chiffres      # Nombre de chiffres désirés
        self.speciaux = speciaux      # Nombre de caractères spéciaux désirés

    def generer(self):
        # Définition des différents types de caractères
        min_chars = 'abcdefghijklmnopqrstuvwxyz'
        maj_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num_chars = '0123456789'
        special_chars = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'

        mdp = ""  # Initialise la chaîne du mot de passe à vide

        # Ajout des caractères minuscules au mot de passe
        for i in range(self.minuscules):
            mdp += random.choice(min_chars)

        # Ajout des caractères majuscules au mot de passe
        for i in range(self.majuscules):
            mdp += random.choice(maj_chars)

        # Ajout des chiffres au mot de passe
        for i in range(self.chiffres):
            mdp += random.choice(num_chars)

        # Ajout des caractères spéciaux au mot de passe
        for i in range(self.speciaux):
            mdp += random.choice(special_chars)

        # Conversion du mot de passe en liste, mélange des caractères pour plus de sécurité
        mdp_list = list(mdp)
        random.shuffle(mdp_list)
        return ''.join(mdp_list)  # Convertit la liste mélangée en chaîne et la retourne
