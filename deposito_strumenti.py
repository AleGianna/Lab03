import csv
from operator import attrgetter
class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = []  # <--- Fondamentale! Crea lo scaffale vuoto per gli strumenti
        self.prestiti = []   # <--- Fondamentale! Crea lo scaffale vuoto per i prestiti

    def __str__(self):
        # 1. Metodo speciale richiamato automaticamente da Python quando si stampa l'oggetto deposito

        riepilogo = f"Deposito: {self.nome}\nResponsabile: {self.responsabile}\nStrumenti: {len(self.strumenti)}\nPrestiti: {len(self.prestiti)}"
        # 2. Crea una stringa riassuntiva unendo i dati del deposito e contando quanti elementi ci sono nelle liste interne

        return riepilogo
        # 3. Restituisce tassativamente la stringa formattata risultante


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            """Carica gli strumenti dal file CSV e li memorizza nel sistema"""
            # open() lancia automaticamente FileNotFoundError se il file non esiste,
            # soddisfacendo la richiesta della traccia.
            for riga in reader:
                if len(riga) >= 5:
                    # Estrae i dati dalla riga del CSV
                    codice, tipo, marca, anno_acquisto, valore = riga[0], riga[1], riga[2], riga[3], riga[4]

                    # Crea l'oggetto Strumento
                    strumento = Strumenti(codice, tipo, marca, anno_acquisto, valore)

                    # Lo aggiunge alla lista del deposito
                    self.strumenti.append(strumento)

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO
        if not self.strumenti:
            codice = "S1"
        else:
            # Prende l'ultimo strumento, estrae la parte numerica dopo la 'S' e la incrementa
            ultimo_codice = self.strumenti[-1].codice  # es. "S4"
            numero = int(ultimo_codice[1:])  # diventa 4
            codice = f"S{numero + 1}"  # diventa "S5"
        strumento = Strumenti(codice, tipo, marca, anno_acquisto, valore)

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        return sorted(self.strumenti, key=attrgetter('marca'))
    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
class PrestitoStrumenti:
    pass
class Strumenti:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        """Inizializza gli attributi del singolo strumento."""
        self.codice = codice  # Es. "S1"
        self.tipo = tipo  # Es. "Chitarra"
        self.marca = marca  # Es. "Yamaha"
        self.anno_acquisto = int(anno_acquisto)  # Convertito in numero intero (es. 2019)
        self.valore = float(valore)  # Convertito in numero decimale (es. 250.00)


    def __str__(self):
        """Rappresentazione testuale leggibile per l'utente (quando usi print)."""
        return f"[{self.codice}] {self.tipo} - {self.marca} ({self.anno_acquisto}) - Valore: €{self.valore:.2f}"