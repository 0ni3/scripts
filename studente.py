# coding=utf-8
class Studente:

    ore = 36 # variabile di classe
    corpo_studentesco = 0

    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1

    def scheda(self):
        return f"Scheda Studente:\n Nome:{self.nome}\n \
        Cognome:{self.cognome}\n \
        Corsi di Studi:{self.corso_di_studi}\n \
        Ore:{self.ore}"

studente_uno = Studente("Paolo", "Rossi", "lettere")
studente_due = Studente("John", "Doe", "matematica")
print("========================")
import pdb; pdb.set_trace()
print(Studente.corpo_studentesco)
print("========================")

studente_uno.ore += 4

print(Studente.scheda(studente_uno))
print(studente_due.scheda())

# la classe è un modello generico per ogni studente creato
# self è l'istanza della classe, ovvero la referenza a n oggetti creati
# il metodo __init__ inizializza e attiva le varie proprietà di ciascun self (oggetto o istanza)
# gli attributi prendono il nome di "variabili dell'istanza"
