from view.player_view import PlayerView
from view.ai_view import AIView
from controller.prolog_controller import PrologController

class GameView:
    '''Gestore del gioco'''

    prolog = PrologController()       # Interprete swi-prolog

    mazziere = AIView(prolog)
    giocatori = []                    # lista di PlayerView

    def __init__(self):
        '''COSTRUTTORE
        Chiede il numero di giocatori e istanzia le PlayerView per ogni giocatore
        '''
        print('CIAO, BENVENUTO IN PY E MEZZO\n')
        NoP = int(input('INSERISCI NUMERO DI GIOCATORI: '))
        for _ in range(NoP):
            new_player = PlayerView(self.prolog)
            self.giocatori.append(new_player)

    def crea_mano(self):
        '''Crea una mano giocabile'''
        self.prolog.create_deck()
        for player in self.giocatori:
            player.pesca(self.prolog)
        self.mazziere.pesca(self.prolog)

    def gioca_mano(self):
        '''Gioca una mano giocabile'''
        for player in self.giocatori:
            player.play_hand(self.prolog)
        print('---------------------------------------------------------------------------------------------------------')
        print('\n\tORA E\' IL TURNO DEL MAZZIERE, OCCHIO')
        self.mazziere.play_hand(self.prolog)
        
        for player in self.giocatori:
            winner, puntata = player.reset(self.prolog)
            print(f'\n\tMAZZIERE VS {player.nome} WIN: {winner}: {puntata}euro')
        
        self.mazziere.reset(self.prolog)

    
    def play(self):
        '''Gioco'''
        scelta = 'y'
        while scelta=='y':
            self.crea_mano()
            self.gioca_mano()
            for player in self.giocatori:
                if player.loose(self.prolog):
                    self.giocatori.remove(player) 
            print('----------------------------------------------------------------')               
            scelta = input('\nVOLETE CONTINUARE A GIOCARE? scegli y/n: ')
