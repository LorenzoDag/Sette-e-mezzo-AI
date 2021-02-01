from pyswip import Prolog, Functor

class PrologController(Prolog):
    '''Controller dei predicati swi-prolog, estende la classe Prolog del modulo pyswip'''
    def __init__(self):
        '''COSTRUTTORE
        Lancia il costruttore della superclasse Prolog e consulta i file .pl del gioco 7 e mezzo
        '''
        super(PrologController, self).__init__()
        self.consult('controller/regole.pl')
        self.consult('controller/carte.pl')
        self.consult('controller/controller.pl')

    def create_deck(self):
        '''Crea e setta l'attributo contenente il mazzo di carte mischiato randomicamente e la lista delle carte uscite'''
        # costuisce il deck mischiato randomicamente

        result = self.query('create_deck(D)')

        for deck in result:
            self.mazzo = deck['D']
            self.uscite = []
        

    def draw_card(self):
        '''Pesca una carta dal mazzo di carte, setta l'attributo prima contenente la carta pescata e la aggiunge alle carte uscite'''
        # pesca una carta dal mazzo
        mazzostr = '['
        if len(self.mazzo) > 0 :
            for card in self.mazzo:
                mazzostr += str(card)+','
            mazzostr = mazzostr[:-1] + ']'
        else:
            mazzostr +=  ']'

        result = self.query('draw_card('+mazzostr+', Prima, Resto)')
        for r in result:
            prima = r['Prima']
            self.mazzo = r['Resto']
        prima = prima.replace('card(', '').replace(' ', '').replace(')', '').split(',')
        self.prima = Functor('card', 2, prima)
        self.uscite.append(self.prima)

    def valore(self, lista_di_funtori):
        '''Lancia il goal per il calcolo del valore delle carte e ne ritorna il punteggio
        
        :type lista_di_funtori: list
        :param lista_di_funtori: Lista contenente oggetti della classe Functor di pyswip rappresentanti le carte

        :return float: valore delle carte 
        '''
        if not isinstance(lista_di_funtori, list):
            raise ValueError('OCCHIO, BISOGNA PASSARE A VALORE UNA LISTA')
        elif len(lista_di_funtori) == 0:
            return 0
        elif not isinstance(lista_di_funtori[0], Functor) and len(lista_di_funtori) != 0:
            raise ValueError('OCCHIO, BISOGNA PASSARE A VALORE UNA LISTA DI FUNTORI!!!')
        else:
            cartestr = '['
            if len(lista_di_funtori) > 0:
                for card in lista_di_funtori:
                    cartestr += str(card) + ','
                cartestr = cartestr[:-1] + ']'
            else:
                cartestr += ']'

            result = self.query('valore('+cartestr+', Value)')

            for i in result:
                return i['Value']

    def who_win(self,Nome):
        '''Lancia il goal per la valutazione del vincitore
        
        :type Nome: string
        :param Nome: Nome del giocatore che sta giocando contro il mazziere

        :return string: nome del vinciore
        '''
        if not isinstance(Nome, str):
            raise ValueError('no')
        result = self.query('who_win(mazziere,'+Nome+',Winner)')
        for player in result :
            winner = player['Winner']
        return winner

    def get_win_mazziere(self):
        '''Lancia il goal per il calcolo della vincita attuale del vincita_mazziere
        
        :return float: +/-vincita attuale del mazziere 
        '''
        result = self.query('vincita_mazziere(V)')
        for r in result :
            win = r['V']
        return win   

    def get_winnable_bet(self):
        '''Torna la puntata totale che il mazziere può vincere o perdere'''
        result = self.query('get_perdita_totale(V)')
        for r in result :
            return r['V']
        return 0

    def get_vincita_miglioramento(self):
        '''Torna la vincita del mazziere se migliorasse la sua situazione'''
        result = self.query('get_vincita_miglioramento(V)')
        for r in result :
            return r['V']
        return 0 

    def min_score(self):
        '''Torna il minimo punteggio da battere if 0 hai vinto'''
        result = self.query('min_score(V)')
        for r in result :
            return r['V']
        return 0 

    def max_score(self):
        '''Torna il massimo punteggio da battere if 0 hai vinto'''
        result = self.query('max_score(V)')
        for r in result :
            return r['V']
        return 0 

    def get_utility(self):
        result = self.query('giocatore(Nome,_,_,Puntata, Punteggio), \+Nome=mazziere')
        vs_score = []
        utility = []
        for r in result: 
            vs_score.append(r['Punteggio'])
            utility.append(r['Puntata'])
        return vs_score, utility

    def get_gain(self):
        result = self.query('giocatore(mazziere,_,_,_,Punteggio_m),giocatore(_,_,_,Puntata,Punteggio),Punteggio > Punteggio_m, Punteggio =< 7.5')
        punteggi = []
        puntate = []
        for i in result:
            puntate.append(i['Puntata'])
            punteggi.append(i['Punteggio'])
        return puntate, punteggi
