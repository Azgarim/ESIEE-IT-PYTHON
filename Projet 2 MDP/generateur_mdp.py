# generateur_mdp.py

import random


def generer_mdp(nb_minuscules, nb_majuscules, nb_chiffres, nb_caracteres_speciaux):
    #Génère un mot de passe basé sur les critères fournis

    minuscules = 'abcdefghijklmnopqrstuvwxyz'
    majuscules = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chiffres = '0123456789'
    caracteres_speciaux = '!@#$%^&*()-_=+[]{}|;:,.<>?/\\'

    mdp = ""

    # Ajouter les minuscules
    for i in range(nb_minuscules):
        mdp += random.choice(minuscules)

    # Ajouter les majuscules
    for i in range(nb_majuscules):
        mdp += random.choice(majuscules)

    # Ajouter les chiffres
    for i in range(nb_chiffres):
        mdp += random.choice(chiffres)

    # Ajouter les caractères spéciaux
    for i in range(nb_caracteres_speciaux):
        mdp += random.choice(caracteres_speciaux)

    # Mélanger le mot de passe pour plus de sécurité
    mdp_list = list(mdp)
    random.shuffle(mdp_list)
    mdp = ''.join(mdp_list)

    return mdp
