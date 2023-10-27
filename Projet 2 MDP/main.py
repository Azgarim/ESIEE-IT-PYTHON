import generateur_mdp
import generateur_phrase
import testeur_mdp

def main():
    while True:
        print("\n1. Tester un mot de passe")
        print("2. Générer un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")

        choix = input("\nChoisissez une option: ")

        if choix == "1":
            mdp = input("\nEntrez le mot de passe à tester: ")
            testeur = testeur_mdp.TesteurMDP(mdp)
            entropie, force = testeur.evaluer()
            print(f"Entropie du mot de passe: {entropie:.2f}")
            print(f"Force du mot de passe: {force}")

        elif choix == "2":
            while True:
                try:
                    minuscules = int(input("Nombre de minuscules: "))
                    if minuscules < 0:
                        raise ValueError("Le nombre ne peut pas être négatif!")
                    break
                except ValueError as e:
                    print(f"Erreur : Veuillez rentrer un nombre")

            while True:
                try:
                    majuscules = int(input("Nombre de majuscules: "))
                    if majuscules < 0:
                        raise ValueError("Le nombre ne peut pas être négatif!")
                    break
                except ValueError as e:
                    print(f"Erreur : Veuillez rentrer un nombre")

            while True:
                try:
                    chiffres = int(input("Nombre de chiffres: "))
                    if chiffres < 0:
                        raise ValueError("Le nombre ne peut pas être négatif!")
                    break
                except ValueError as e:
                    print(f"Erreur : Veuillez rentrer un nombre")

            while True:
                try:
                    speciaux = int(input("Nombre de caractères spéciaux: "))
                    if speciaux < 0:
                        raise ValueError("Le nombre ne peut pas être négatif!")
                    break
                except ValueError as e:
                    print(f"Erreur : Veuillez rentrer un nombre")

            generateur = generateur_mdp.GenerateurMDP(minuscules, majuscules, chiffres, speciaux)
            mdp = generateur.generer()

            print(f"Mot de passe généré: {mdp}")

            testeur = testeur_mdp.TesteurMDP(mdp)
            entropie, force = testeur.evaluer()
            print(f"Entropie du mot de passe: {entropie:.2f}")
            print(f"Force du mot de passe: {force}")

        elif choix == "3":
            generateur = generateur_phrase.GenerateurPhrase()
            phrase = generateur.generer()

            print(f"Passphrase générée: {phrase}")

            testeur = testeur_mdp.TesteurMDP(phrase)
            entropie, force = testeur.evaluer()
            print(f"Entropie du mot de passe: {entropie:.2f}")
            print(f"Force du mot de passe: {force}")

        elif choix == "4":
            break
        else:
            print("Veuillez choisir une option valide!")

if __name__ == "__main__":
    main()
