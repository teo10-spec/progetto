
# Esercizio 1
titolo = "Il Signore degli Anelli"   
copie = 5                             
prezzo_medio = 18.50                  
disponibile = copie > 0 

print("Titolo:", titolo)
print("Copie disponibili:", copie)
print("Prezzo medio:", prezzo_medio)

if disponibile:
    print("Stato: Disponibile ")
else:
    print("Stato: Non disponibile ")

# Secondo libro
titolo = "Il Signore degli Anelli"  
copie = 0                           
prezzo_medio = 18.50                  
disponibile = copie > 0  

print("\nTitolo:", titolo)
print("Copie disponibili:", copie)
print("Prezzo medio:", prezzo_medio)

if disponibile:
    print("Stato: Disponibile ")
else:
    print("Stato: Non disponibile ")


# Esercizio 2
lista_libri = [
    "Il Signore degli Anelli",
    "Harry Potter",
    "1984",
    "Il Piccolo Principe",
    "Lo Hobbit"
]

copie_libri = {
    "Il Signore degli Anelli": 5,
    "Harry Potter": 3,
    "1984": 4,
    "Il Piccolo Principe": 2,
    "Lo Hobbit": 1
}

utenti_registrati = {"Mario", "Luisa", "Giulia", "Paolo"}

print("\nLista libri:", lista_libri)
print("Copie libri:", copie_libri)
print("Utenti registrati:", utenti_registrati)


# Classi
class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self):
        print(f"Libro → Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}")


class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self):
        print(f"Scheda Utente → Nome: {self.nome}, Età: {self.eta}, ID Utente: {self.id_utente}")


class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self):
        print(f"Prestito → Utente: {self.utente.nome}, Libro: {self.libro.titolo}, Giorni: {self.giorni}")


# Creazione oggetti
u1 = Utente("Mario", 25, 1)
l1 = Libro("1984", "Orwell", 1949, 3)

u1.scheda()
l1.info()

p1 = Prestito(u1, l1, 7)
p1.dettagli()
