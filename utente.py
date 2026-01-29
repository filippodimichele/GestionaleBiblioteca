class Utente:
    def __init__(self, nome, numero_tessera):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.prestiti = []
        
    def aggiungi_prestiti(self, prestiti):
        self.prestiti = prestiti
        
    def storico_prestiti(self):
        return self.prestiti
    
    #max 3 prestiti
    def __str__(self):
        return f"{self.nome} (Tessera {self.numero_tessera})"