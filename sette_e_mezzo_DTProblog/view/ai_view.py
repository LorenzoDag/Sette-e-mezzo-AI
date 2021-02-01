from controller.ai_controller import AIController
from format.card_formatter import CardFormatter

from time import sleep

class AIView(AIController):
    '''View del mazziere'''

    f = CardFormatter()

    def __init__(self, prolog):
        '''COSTRUTTORE

        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        super(AIView, self).__init__('mazziere', 100000, prolog)

    def play_hand(self, prolog):
        '''Formatta le giocate dell'intelligenza artificiale in riga di comando'''
        print(f'IL MAZZIERE HA {self.punteggio} PUNTI')
        print(f'CARTE: \t{self.f.format(self.carte)}')
        while self.decidi(prolog):
            try:
                print("\n\tPESCO UNA CARTA")
                self.pesca(prolog)
                print(f"PUNTEGGIO {self.punteggio}")
                print(f'CARTE: \t{self.f.format(self.carte)}')
                if self.punteggio > 7.5:
                    print('\n\tIL MAZZIERE HA SBALLATO, GRANDE FESTA!!')
                    break
                elif self.punteggio == 7.5:
                    print('\nOH OH! IL MAZZIERE HA FATTO 7 E MEZZO, FRECHETE!')
                sleep(3)
            except Exception as e:
                print(e)
                break