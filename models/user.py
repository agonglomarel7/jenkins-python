# models/user.py
"""
MODEL - Représente la structure des données
Le modèle User contient les informations d'un utilisateur
"""

class User:
    """Classe qui représente un utilisateur"""
    
    def __init__(self, nom, prenom, email):
        """
        Initialise un nouvel utilisateur
        
        Args:
            nom (str): Nom de famille
            prenom (str): Prénom
            email (str): Adresse email
        """
        self.nom = nom
        self.prenom = prenom
        self.email = email
    
    def __str__(self):
        """Retourne une représentation en texte de l'utilisateur"""
        return f"{self.prenom} {self.nom} ({self.email})"
    
    def get_full_name(self):
        """Retourne le nom complet de l'utilisateur"""
        return f"{self.prenom} {self.nom}"
    
    def to_dict(self):
        """Convertit l'utilisateur en dictionnaire"""
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email
        }