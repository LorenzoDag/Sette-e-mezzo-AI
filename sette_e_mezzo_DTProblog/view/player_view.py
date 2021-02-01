from controller.player_controller import PlayerController
from format.card_formatter import CardFormatter

class PlayerView(PlayerController):
    f = CardFormatter()
    '''View dei giocatori'''

    def __init__(self, prolog, mazziere = False):
        '''COSTRUTTORE
        Chiama il costruttore della superclasse PlayerController dopo aver chiesto di inserire nome e soldi del giocatore
        
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        if not mazziere:
            nome = input('INSERISCI NOME GIOCATORE: ')
            try:
                soldi = float(input(f"\t{nome}, INSERISCI QUANTI SOLDI HAI A DISPOSIZIONE: "))
                super(PlayerView, self).__init__(nome, soldi, prolog)
            except ValueError:
                print('ATTENZIONE, DEVI INSERIRE UN NUMERO PER I TUOI SOLDI!')
                self.__init__(prolog)
        else:
            super(PlayerView, self).__init__('mazziere', 100000, prolog)

    def play_hand(self, prolog):
        '''Formatta le richieste delle giocate ai giocatori e lancia i metodi del controller'''
        try:
            if not self.nome == 'mazziere':
                print('---------------------------------------------------------------------------------------------------------')
                puntata = float(input(f'{self.nome}, HAI {self.soldi}euro E {self.punteggio} PUNTI.\nCARTE: {self.f.format(self.carte)}\n\tINSERISCI LA PUNTATA: '))
                while not self.punta(puntata, prolog):
                    puntata = float(input(f'\n\tINSERISCI LA PUNTATA: '))
            
            scelta = input(f'\n\tHAI {self.punteggio} PUNTI\nCARTE: {self.f.format(self.carte)}\n\tVUOI PESCARE ANCORA? scelta y/n: ')
            while scelta == 'y':
                self.pesca(prolog)
                if self.punteggio > 7.5:
                    print(f'\tOH OH!! HAI SBALLATO: {self.f.format(self.carte)}, PUNTEGGIO: {self.punteggio}')
                    break
                elif self.punteggio == 7.5:
                    print(f'\nCARTE: {self.f.format(self.carte)}')
                    input("\tHAI FATTO 7 E MEZZO, COMPLIMENTSSS!!!")
                    break
                else:
                    scelta = input(f'\n\tHAI {self.punteggio} PUNTI\nCARTE: {self.f.format(self.carte)}\n\tVUOI PESCARE ANCORA? scelta y/n: ')
        except ValueError:
            print('ATTENZIONE, DEVI PUNTARE UN NUMERO!')
            self.play_hand(prolog)

    def loose(self, prolog):
        '''Controlla se un giocatore ha perso e chiede se vuole rientrare'''
        if self.soldi == 0:
            scelta = input(f'\n\t{self.nome}, HAI FINITO I SODI. VUOI RIENTRARE? y/n: ')
            if scelta == 'y':
                self.remove_from_db(prolog)
                self.soldi = float(input('\tOK, INSERISCI I TUOI SOLDI: '))
                self.add_to_db(prolog)
                return False
            else:
                self.delete(prolog)
                return True
        else:
            return False
