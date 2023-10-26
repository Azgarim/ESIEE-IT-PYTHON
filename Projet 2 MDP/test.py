import unittest
from generateur_mdp import generer_mdp
from generateur_phrase import generer_phrase, lancer_des
from testeur_mdp import evaluer_mdp
import math

class TestOutils(unittest.TestCase):

    # Test pour le générateur de mot de passe
    def test_generer_mdp(self):
        mdp = generer_mdp(4, 2, 2, 2)
        self.assertEqual(len(mdp), 10)  # Vérifie la longueur du mot de passe généré

    # Test pour le générateur de passphrase
    def test_generer_passphrase(self):
        passphrase = generer_phrase().split("-")
        with open("eff_large_wordlist.txt", "r") as f:
            mots = f.read().splitlines()
            mots = [line.split()[1] for line in mots]
        for mot in passphrase:
            self.assertIn(mot, mots)  # Vérifie si chaque mot est présent dans le fichier

    # Test pour lancer des
    def test_lancer_des(self):
        resultat = lancer_des()
        self.assertEqual(len(resultat), 5)  # Vérifie la longueur du résultat
        for char in resultat:
            self.assertIn(char, "123456")  # Vérifie que chaque caractère est un chiffre entre 1 et 6

        # Test pour le calcul de l'entropie

    def test_evaluer_mdp(self):
        mdp = "A1b2C3"
        entropie, force = evaluer_mdp(mdp)
        expected_entropie = len(mdp) * math.log2(62)  # 26 minuscules + 26 majuscules + 10 chiffres
        self.assertAlmostEqual(entropie, expected_entropie)
        self.assertEqual(force, "très faible")  # Avec notre exemple, la force doit être "très faible"


if __name__ == "__main__":
    unittest.main()