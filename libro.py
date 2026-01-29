class Libro:
    def __init__(self,titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.disponibile = True
        
        
    def _isdisponibile(self, disponibile):
        return self._isdisponibile
    
    def prestito(self):
        self.disponibile = False
        
    def restituisci(self):
        self.disponibile = True
        
        
    def __str__(self):
        stato = "Disponibile" if self.disponibile else "In prestito"