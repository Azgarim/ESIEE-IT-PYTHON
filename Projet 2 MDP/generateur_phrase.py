import random

class GenerateurPhrase:
    # Constructeur de la classe, initialisé avec le nombre de mots souhaité pour la phrase secrète
    def __init__(self, n_mots=6):
        self.n_mots = n_mots

    # Méthode pour simuler le lancement de 5 dés, renvoie une chaîne de 5 chiffres
    def lancer_des(self):
        resultat = ""
        for _ in range(5):
            resultat += str(random.randint(1, 6))
        return resultat

    # Méthode pour chercher un mot dans le fichier "eff_large_wordlist.txt" basé sur un indice donné
    def chercher_mot(self, indice):
        # Ouverture du fichier en mode lecture
        with open("eff_large_wordlist.txt", "r") as f:
            # Parcourt chaque ligne du fichier
            for line in f:
                # Si une ligne commence par l'indice donné, retourne le mot associé
                if line.startswith(indice):
                    return line.split()[1]

    # Méthode principale pour générer une phrase secrète
    def generer(self):
        phrase = ""
        # Génération des mots pour la phrase
        for i in range(self.n_mots):
            indice = self.lancer_des()       # Obtention de l'indice via le lancement des dés
            mot = self.chercher_mot(indice)  # Recherche du mot correspondant à l'indice
            phrase += mot + '-'              # Ajout du mot à la phrase avec un séparateur '-'
        return phrase[:-1]  # Retour de la phrase sans le dernier séparateur '-'
