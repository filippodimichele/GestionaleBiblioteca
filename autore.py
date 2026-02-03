class Autore:

    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita

    def __repr__(self):
        return f"Autore(nome='{self.nome}', nazionalita='{self.nazionalita}')"

    def __eq__(self, other):
        if not isinstance(other, Autore):
            return False
        return self.nome == other.nome and self.nazionalita == other.nazionalita