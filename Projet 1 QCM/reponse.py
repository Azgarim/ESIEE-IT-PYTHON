class Reponse:
    def __init__(self, texte, est_correcte=False):
        # Initialisation des attributs pour le texte de la réponse et pour savoir si elle est correcte
        self.texte = texte
        self.est_correcte = est_correcte
