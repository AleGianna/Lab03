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
            header = next(reader, None)
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
        if not self.strumenti:
            codice = "S1"
        else:
            # Prende l'ultimo strumento, estrae la parte numerica dopo la 'S' e la incrementa
            ultimo_codice = self.strumenti[-1].codice  # es. "S4"
            numero = int(ultimo_codice[1:])  # diventa 4
            codice = f"S{numero + 1}"  # diventa "S5"
        strumento = Strumenti(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)
        return strumento
    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # self.strumenti serve per richiamare la lista di oggetti e si puo fare solo all'interno della classe in cui vi è la lista
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        if id_strumento in [s.codice for s in self.strumenti] :
            if id_strumento not in [p.id_strumento for p in self.prestiti]:
                if not self.prestiti:
                    id_prestito = "P1"
                else:
                    # Prende l'ultimo strumento, estrae la parte numerica dopo la 'S' e la incrementa
                    ultimo_codice = self.prestiti[-1].id_prestito  # es. "S4"
                    numero = int(ultimo_codice[1:])  # diventa 4
                    id_prestito = f"P{numero + 1}"  # diventa "S5"
                prestito = PrestitoStrumenti(id_prestito, data, id_strumento, cognome_allievo)
                self.prestiti.append(prestito)
                return id_prestito
            else:
                raise Exception(f"Lo strumento {id_strumento} e' gia' stato prestato.")
        else:
            raise Exception (f"Lo strumento {id_strumento} non esiste nel deposito.")

    def termina_prestito(self, id_prestito):
        g=False
        for p in self.prestiti:
            if p.id_prestito == id_prestito:
                self.prestiti.remove(p)
                g=True
                break
        if not g:
            raise Exception (f"il prestito {id_prestito} non esiste nel registro.")


class PrestitoStrumenti:
    def __init__(self, id_prestito, data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        """Rappresentazione testuale leggibile per l'utente (quando usi print)."""
        return f"[{self.id_prestito}] {self.data} - {self.id_strumento} ({self.cognome_allievo})"



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