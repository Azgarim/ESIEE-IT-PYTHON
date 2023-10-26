# Générateur et Testeur de Mot de Passe

Ce projet fournit des outils pour générer des mots de passe aléatoires solides et pour tester la force des mots de passe selon les critères de l'ANSSI.

## Fonctionnalités

1. **Testeur de mot de passe** : Évalue la force d'un mot de passe en se basant sur son entropie.
2. **Générateur de mot de passe** : Crée un mot de passe aléatoire en fonction des critères sélectionnés par l'utilisateur (nombre de minuscules, majuscules, chiffres, caractères spéciaux).
3. **Générateur de passphrase** : Utilise la méthode de dés de l'EFF pour générer une passphrase robuste.

## Comment l'utiliser

1. Clonez ce dépôt git.
2. Exécutez `main.py` pour lancer l'application.
3. Suivez les instructions à l'écran pour générer ou tester un mot de passe.

## Critères de l'ANSSI

La force d'un mot de passe est déterminée selon les critères de l'ANSSI :
- Très faible : < 64 bits d'entropie
- Faible : entre 64 et 80 bits
- Moyen : entre 80 et 100 bits
- Fort : > 100 bits

---

Antoine NOURY
