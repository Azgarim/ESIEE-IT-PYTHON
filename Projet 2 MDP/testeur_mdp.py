import math


def calculer_entropie(mdp):
    #Calcule l'entropie du mot de passe basé sur son alphabet

    longueur = len(mdp)

    # Définir les alphabets
    minuscules = 'abcdefghijklmnopqrstuvwxyz'
    majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chiffres = '0123456789'
    caracteres_speciaux = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'

    # Déterminer l'alphabet utilisé
    taille_alphabet = 0
    if any(c in minuscules for c in mdp):
        taille_alphabet += len(minuscules)
    if any(c in majuscules for c in mdp):
        taille_alphabet += len(majuscules)
    if any(c in chiffres for c in mdp):
        taille_alphabet += len(chiffres)
    if any(c in caracteres_speciaux for c in mdp):
        taille_alphabet += len(caracteres_speciaux)

    # Calculer l'entropie
    entropie = longueur * math.log2(taille_alphabet)

    return entropie


def evaluer_force(entropie):
    #Évalue la force du mot de passe basée sur son entropie
    if entropie < 64:
        return "très faible"
    elif 64 <= entropie < 80:
        return "faible"
    elif 80 <= entropie < 100:
        return "moyen"
    else:
        return "fort"


def tester_mdp(mdp):
    #Teste la force du mot de passe
    entropie = calculer_entropie(mdp)
    force = evaluer_force(entropie)

    return entropie, force
