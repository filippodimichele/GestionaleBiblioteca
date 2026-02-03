from autore import Autore
from libro import Libro
from utente import Utente
from biblioteca import Biblioteca


def main():
    # Creazione biblioteca
    print("--- CREAZIONE BIBLIOTECA ---")
    biblioteca = Biblioteca("Biblioteca Comunale di Pescara")
    print(biblioteca)

    # Creazione autori
    print("\n--- CREAZIONE AUTORI ---")
    calvino = Autore("Italo Calvino", "Italia")
    orwell = Autore("George Orwell", "Regno Unito")
    marquez = Autore("Gabriel Garcia Marquez", "Colombia")
    print(calvino)
    print(orwell)
    print(marquez)

    # Aggiunta libri al catalogo
    print("\n--- AGGIUNTA LIBRI ---")
    libro1 = Libro("Il barone rampante", "978-88-04-66123-0", calvino)
    libro2 = Libro("Le citta invisibili", "978-88-04-66124-7", calvino)
    libro3 = Libro("1984", "978-88-04-12345-6", orwell)
    libro4 = Libro("La fattoria degli animali", "978-88-04-12346-3", orwell)
    libro5 = Libro("Cent'anni di solitudine", "978-88-04-99999-9", marquez)

    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)
    biblioteca.aggiungi_libro(libro3)
    biblioteca.aggiungi_libro(libro4)
    biblioteca.aggiungi_libro(libro5)
    biblioteca.aggiungi_libro(libro1)  # Test duplicato

    # Registrazione utenti
    print("\n--- REGISTRAZIONE UTENTI ---")
    utente1 = Utente("Mario Rossi", "T001")
    utente2 = Utente("Laura Bianchi", "T002")

    biblioteca.registra_utente(utente1)
    biblioteca.registra_utente(utente2)
    biblioteca.registra_utente(utente1)  # Test duplicato

    # Ricerca libri
    print("\n--- RICERCA PER TITOLO 'citta' ---")
    for libro in biblioteca.cerca_per_titolo("citta"):
        print(libro)

    print("\n--- RICERCA PER AUTORE 'Calvino' ---")
    for libro in biblioteca.cerca_per_autore("Calvino"):
        print(libro)

    # Libri disponibili
    print("\n--- LIBRI DISPONIBILI ---")
    for libro in biblioteca.libri_disponibili():
        print(libro)

    # Prestiti
    print("\n--- EFFETTUA PRESTITI ---")
    biblioteca.effettua_prestito("978-88-04-66123-0", "T001")
    biblioteca.effettua_prestito("978-88-04-12345-6", "T001")
    biblioteca.effettua_prestito("978-88-04-99999-9", "T002")

    print("\n--- TEST: libro non disponibile ---")
    biblioteca.effettua_prestito("978-88-04-66123-0", "T002")

    print("\n--- TEST: limite prestiti ---")
    biblioteca.effettua_prestito("978-88-04-66124-7", "T001")  # 3° libro
    biblioteca.effettua_prestito("978-88-04-12346-3", "T001")  # 4° libro - fallisce

    # Stato dopo prestiti
    print("\n--- STATO UTENTI ---")
    print(utente1)
    print(utente2)

    print("\n--- LIBRI DISPONIBILI ---")
    for libro in biblioteca.libri_disponibili():
        print(libro)

    # Storico prestiti
    print("\n--- STORICO PRESTITI MARIO ---")
    for prestito in biblioteca.storico_utente("T001"):
        print(prestito)

    # Restituzione
    print("\n--- RESTITUZIONE ---")
    biblioteca.effettua_restituzione("978-88-04-66123-0", "T001")

    print("\n--- TEST: restituzione non valida ---")
    biblioteca.effettua_restituzione("978-88-04-66123-0", "T001")

    # Stato finale
    print("\n--- STATO FINALE ---")
    print(utente1)
    print(f"Libri disponibili: {len(biblioteca.libri_disponibili())}")

    print("\n--- STORICO COMPLETO MARIO ---")
    for prestito in biblioteca.storico_utente("T001"):
        print(prestito)


if __name__ == "__main__":
    main()