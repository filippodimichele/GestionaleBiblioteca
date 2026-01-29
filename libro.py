class Libro:
    def __init__(self,titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.disponibile = True #Se disponibile
        
        
    def _isdisponibile(self, disponibile):
        return self._isdisponibile
    
    def prestito(self):
        self.disponibile = False #il prestito non è disponibile
        
    def restituisci(self):
        self.disponibile = True  # True se restituisce il prestito
        
        
    def __str__(self):
        stato = "Disponibile" if self.disponibile else "In prestito" #Solo se disponibile, altrimenti in prestito