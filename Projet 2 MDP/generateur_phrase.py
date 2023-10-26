import random


def lancer_des():
    #Simule le lancer de 5 dés pour obtenir un indice
    resultat = ""
    for _ in range(5):
        resultat += str(random.randint(1, 6))
    return resultat


def chercher_mot(indice):
    #Cherche un mot dans la liste EFF basé sur l'indice fourni.
    f = open("eff_large_wordlist.txt", "r")
    lines = f.readlines()
    for line in lines:
        if line.startswith(indice):
            mot = line.split()[1] #Utilise le deuxième mot de la ligne c'est à dire le mot que l'on cherche
            f.close()
            return mot
    f.close()

def generer_phrase():
    #Génère une passphrase à partir de 6 mots
    phrase = ""
    for i in range(6):
        indice = lancer_des()
        mot = chercher_mot(indice)
        phrase += mot
        if i < 5:
            phrase += "-"
    # [1:] #Supprime le dernier caractère et le premier qui se fait déplacer depuis la dernière position
    return phrase.strip()
