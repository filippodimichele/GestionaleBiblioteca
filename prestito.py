class Prestito:
    def __init__(self, libro, utente, data_prestito):
        self.libro = libro
        self.utente = utente 
        self.data_prestito = data_prestito
        self.data_restituzione = None
        
    def chiudi(self, data_restituzione):
        self.data_restituzione = data_restituzione
    
    def is_attivo(self):
        return self.data_restituzione is None
    
    def __str__(self):
        if self.is_attivo # mancano i due return con libro.titolo, data.prestito e data.restituzione
   

