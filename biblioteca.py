from prestito import Prestito


class Biblioteca:

    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        self.utenti = []
        self.storico_prestiti = []

    def __repr__(self):
        return f"Biblioteca(nome='{self.nome}', libri={len(self.catalogo)}, utenti={len(self.utenti)})"

    def aggiungi_libro(self, libro):
        if libro in self.catalogo:
            print(f"Il libro '{libro.titolo}' e' gia' presente nel catalogo.")
            return False
        self.catalogo.append(libro)
        print(f"Libro '{libro.titolo}' aggiunto al catalogo.")
        return True

    def registra_utente(self, utente):
        if utente in self.utenti:
            print(f"L'utente '{utente.nome}' e' gia' registrato.")
            return False
        self.utenti.append(utente)
        print(f"Utente '{utente.nome}' registrato con tessera '{utente.numero_tessera}'.")
        return True

    def _trova_libro(self, isbn):
        for libro in self.catalogo:
            if libro.isbn == isbn:
                return libro
        return None

    def _trova_utente(self, numero_tessera):
        for utente in self.utenti:
            if utente.numero_tessera == numero_tessera:
                return utente
        return None

    def effettua_prestito(self, isbn, numero_tessera):
        libro = self._trova_libro(isbn)
        if not libro:
            print(f"Libro con ISBN '{isbn}' non trovato.")
            return False

        utente = self._trova_utente(numero_tessera)
        if not utente:
            print(f"Utente con tessera '{numero_tessera}' non trovato.")
            return False

        if not libro.disponibile:
            print(f"Il libro '{libro.titolo}' non e' disponibile.")
            return False

        if not utente.puo_prendere_in_prestito():
            print(f"L'utente '{utente.nome}' ha raggiunto il limite di {utente.MAX_PRESTITI} prestiti.")
            return False

        prestito = Prestito(libro, utente)
        libro.presta()
        utente.aggiungi_prestito(prestito)
        self.storico_prestiti.append(prestito)

        print(f"Prestito effettuato: '{libro.titolo}' a '{utente.nome}'.")
        return True

    def effettua_restituzione(self, isbn, numero_tessera):
        libro = self._trova_libro(isbn)
        if not libro:
            print(f"Libro con ISBN '{isbn}' non trovato.")
            return False

        utente = self._trova_utente(numero_tessera)
        if not utente:
            print(f"Utente con tessera '{numero_tessera}' non trovato.")
            return False

        prestito_trovato = None
        for prestito in utente.prestiti:
            if prestito.libro == libro and prestito.is_attivo():
                prestito_trovato = prestito
                break

        if not prestito_trovato:
            print(f"Nessun prestito attivo trovato per '{libro.titolo}' e '{utente.nome}'.")
            return False

        prestito_trovato.concludi()
        libro.restituisci()
        utente.rimuovi_prestito(prestito_trovato)

        print(f"Restituzione effettuata: '{libro.titolo}' da '{utente.nome}'.")
        return True

    def cerca_per_titolo(self, titolo):
        risultati = []
        titolo_lower = titolo.lower()
        for libro in self.catalogo:
            if titolo_lower in libro.titolo.lower():
                risultati.append(libro)
        return risultati

    def cerca_per_autore(self, nome_autore):
        risultati = []
        nome_lower = nome_autore.lower()
        for libro in self.catalogo:
            if nome_lower in libro.autore.nome.lower():
                risultati.append(libro)
        return risultati

    def libri_disponibili(self):
        return [libro for libro in self.catalogo if libro.disponibile]

    def storico_utente(self, numero_tessera):
        utente = self._trova_utente(numero_tessera)
        if not utente:
            print(f"Utente con tessera '{numero_tessera}' non trovato.")
            return []

        storico = []
        for prestito in self.storico_prestiti:
            if prestito.utente == utente:
                storico.append(prestito)
        return storico