class CardFormatter:
    '''Formattatore delle carte in riga di comando'''
    semi = {
        'denari': 'd',
        'bastoni': 'b',
        'coppe': 'c',
        'spade': 's'
    }

    def __init__(self):
        pass

    def format(self, listof_cards):
        '''Ritorna la lista di stringhe rappresentanti le carte
        
        :type listof_cards: list
        :param listof_cards: lista contenente le stringhe rappresentanti i funtori delle carte

        :return list: lista di stringhe delle carte, es ['card(10, denari)'] -> ['10d']
        '''
        str_lista= []
        for c in listof_cards:
            c=str(c)
            c=c.replace('card(','').replace(' ','').replace(')', '')
            c = c.split(',')
            stringa_c = str(c[0])+self.semi[c[1]]
            str_lista.append(stringa_c)
        return str_lista