class Autore:

    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita
        
    def __str__(self):
         return f"{self.nome} ({self.nazionalita})" 