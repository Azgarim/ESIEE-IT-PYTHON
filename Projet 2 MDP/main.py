# main.py
import testeur_mdp
import generateur_mdp
import generateur_phrase


def main():
    while True:
        print("\n1. Tester un mot de passe")
        print("2. Générer un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")

        choix = input("\nChoisissez une option: ")

        if choix == "1":
            mdp = input("\nEntrez le mot de passe à tester: ")
            entropie, force = testeur_mdp.tester_mdp(mdp)
            print(f"Entropie du mot de passe: {entropie:.2f}") #Affiche l'entropie avec 2 chiffres derrière la virgule
            print(f"Force du mot de passe: {force}")

        elif choix == "2":
            minuscules = int(input("Nombre de minuscules: "))
            majuscules = int(input("Nombre de majuscules: "))
            chiffres = int(input("Nombre de chiffres: "))
            speciaux = int(input("Nombre de caractères spéciaux: "))
            mdp = generateur_mdp.generer_mdp(minuscules, majuscules, chiffres, speciaux)
            print(f"Mot de passe généré: {mdp}")
            entropie, force = testeur_mdp.tester_mdp(mdp)
            print(f"Entropie du mot de passe: {entropie:.2f}")  # Affiche l'entropie avec 2 chiffres derrière la virgule
            print(f"Force du mot de passe: {force}")

        elif choix == "3":
            phrase = generateur_phrase.generer_phrase()
            print(f"Passphrase générée: {phrase}")
            entropie, force = testeur_mdp.tester_mdp(phrase)
            print(f"Entropie du mot de passe: {entropie:.2f}")  # Affiche l'entropie avec 2 chiffres derrière la virgule
            print(f"Force du mot de passe: {force}")

        elif choix == "4":
            break


if __name__ == "__main__":
    main()
