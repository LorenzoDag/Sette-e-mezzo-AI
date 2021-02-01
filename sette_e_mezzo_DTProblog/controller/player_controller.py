from model.player_model import PlayerModel


class PlayerController(PlayerModel):
    '''Controller del giocatore. 
    Contiene tutti i metodi per la gestione del database swi-prolog del giocatore    
    '''
    def __init__(self, nome, soldi, prolog):
        '''COSTRUTTORE
        chiama il costruttore della superclasse PlayerModel e aggiunge il giocatore risultante al database prolog

        :type nome: string
        :param nome: nome del giocatore
        :type soldi: float
        :param soldi: soldi del giocatore 
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        super(PlayerController, self).__init__(nome,soldi,prolog)
        self.add_to_db(prolog)

    def pesca(self, prolog):
        '''Il giocatore pesca una carta e aggiorna il database

        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        prolog.draw_card()
        self.remove_from_db(prolog)
        self.carte.append(prolog.prima)
        if len(self.carte) == 1 and self.carte[0] == 'card(10, denari)':
            self.punteggio = 0.5
        else:
            self.punteggio = prolog.valore(self.carte)
        self.add_to_db(prolog)

    def punta(self, puntata, prolog):
        '''Il giocatore effettua una puntata e aggiorna il database

        :type puntata: float
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip

        :return bool: true se la puntata è fattibile, false altrimenti
        '''
        if puntata <= self.soldi:
            self.remove_from_db(prolog)
            self.puntata = puntata
            self.soldi -= puntata
            self.add_to_db(prolog)
            return True
        else:
            print('OCCHIO: NON PUOI PUNTARE PIU DI QUANTO DISPONI')
            return False
    
    def reset(self, prolog):
        '''Reset del giocatore con la valutazione della vincita

        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
       
        if not self.nome == 'mazziere':
            winner = prolog.who_win(self.nome)
            self.remove_from_db(prolog)
            p = self.puntata
            if winner == self.nome:
                self.soldi += 2*self.puntata
        else:
            self.remove_from_db(prolog)
        self.carte = []
        self.punteggio = 0
        self.puntata = 0
        if not self.nome == 'mazziere':               
            self.add_to_db(prolog)   
            return winner, p
        else:
            self.add_to_db(prolog)
            return None

    def add_to_db(self, prolog):
        '''Aggiunge il giocatore al database
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        prolog.asserta(str(self))
    def remove_from_db(self, prolog):
        '''Rimuove il giocatore dal database
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        prolog.retract(str(self))

    def delete(self, prolog):
        '''Elimina il giocatore'''
        self.remove_from_db(prolog)
        print(f'\n\tCIAO CIAO {self.nome}, E\' STATO UN PIACERE GIOCARE CON TE')
        del self