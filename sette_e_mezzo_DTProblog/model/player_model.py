class PlayerModel:
    '''Il modello del giocatore nel sette e mezzo, swi-prolog -> giocatore(Nome, Carte, Soldi, Puntata, Punteggio)'''
    def __init__(self, nome, soldi, prolog):
        '''COSTRUTTORE
        Inizializza gli attributi della clsse.

        :type nome: string
        :param nome: nome del giocatore
        :type soldi: float
        :param soldi: soldi del giocatore 
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip

        '''
        self.nome = nome
        self.carte = []
        self.soldi = soldi
        self.puntata = 0
        self.punteggio = prolog.valore(self.carte)

    def to_string(self, search_carte=False, search_soldi=False, search_puntata=False, search_punteggio=False):
        '''Torna una stringa contenente il funtore dell'oggetto in prolog,
        es: giocatore(mario, Carte, 10.0, 1.0, 7)

        :type search_carte: bool
        :param search_carte: se True torna la stringa contenente il funtore del giocatore le cui carte sono una variabile in prolog
        :type search_soldi: bool
        :param search_soldi: se True torna la stringa contenente il funtore del giocatore i cui soldi sono una variabile in prolog
        :type search_puntata: bool
        :param search_puntata: se True torna la stringa contenente il funtore del giocatore i cui soldi sono una variabile in prolog
        :type search_punteggio: bool
        :param search_punteggio: se True torna la stringa contenente il funtore del giocatore il cui punteggio è una variabile in prolog

        :return giocatore: es giocatore(mario, [card(10,coppe)], 10.0, 1.0, Punteggio)
        '''
        giocatore = 'giocatore('+self.nome+','
        cartestr = '['
        if len(self.carte) > 0:
            for card in self.carte:
                cartestr += str(card) + ','
            cartestr = cartestr[:-1] + ']'
        else:
            cartestr += ']' 

        giocatore += cartestr+','
        if search_soldi:
            giocatore += 'Soldi,'+str(self.puntata)+','+str(self.punteggio)+')'
        elif search_puntata:
            giocatore += str(self.soldi)+',Puntata,'+str(self.punteggio)+')'
        elif search_punteggio:
            giocatore += str(self.soldi)+','+str(self.puntata)+',Punteggio)'
        else:
            giocatore += str(self.soldi)+','+str(self.puntata)+','+str(self.punteggio)+')'
        
        return giocatore

    def __str__(self):
        '''Torna la stringa contenente il funtore descrittivo del giocatore
        :return giocatore: giocatore(lorenzo, [card(10,denari)], 14.0, 2.0, 0.5)
        '''
        giocatore = 'giocatore('+self.nome+','
        cartestr = '['
        if len(self.carte) > 0:
            for card in self.carte:
                cartestr += str(card) + ','
            cartestr = cartestr[:-1] + ']'
        else:
            cartestr += ']' 

        giocatore += cartestr+','+str(self.soldi)+','+str(self.puntata)+','+str(self.punteggio)+')'
        
        return giocatore
