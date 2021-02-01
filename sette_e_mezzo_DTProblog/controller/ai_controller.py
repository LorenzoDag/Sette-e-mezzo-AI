from controller.player_controller import PlayerController

from problog.program import PrologString
from problog.tasks.dtproblog import dtproblog


from problog.core import ProbLog
from problog.engine import DefaultEngine
from problog import get_evaluatable
from problog.logic import Term,Var,Constant


class AIController(PlayerController):
    '''Intelligenza artificiale

    Contiene i metodi per la gestione delle decisioni prese dal maziere
    '''
    ''' conoscenza del dt_problog'''
    conoscenza = []

    ''' conoscenza del problog (calcolo inferenza) '''
    conoscenza_prob = []
    

    vincita_attuale = 0

    def __init__(self, nome, soldi, prolog):
        '''COSTRUTTORE
        chiama il costruttore della superclasse PlayerController ed istanzia gli oggetti per la gestione delle query problog

        :type nome: string
        :param nome: nome del giocatore
        :type soldi: float
        :param soldi: soldi del giocatore 
        :type prolog: PrologController
        :param prolog: Oggetto PrologController che estende la classe Prolog del modulo pyswip
        '''
        super(AIController, self).__init__(nome, soldi, prolog)
        self.read_file(path = 'controller/dt_problog.pl', path1 = 'controller/knowledge_problog.pl')
        self.learn()
        
        

    def read_file(self, path, path1):
        '''Legge i file .pl contenenti la conoscenza problog e crea una lista contenente tutti i predicati
        '''
        try:
            
            with open(path) as kn_file:
                self.conoscenza = kn_file.read()

            with open(path1) as kn_file:
                for row in kn_file:
                    self.conoscenza_prob.append(row.rstrip('\n'))

            self.conoscenza_prob = list(filter(('').__ne__, self.conoscenza_prob))
                
        except Exception as e: 
            print(e)

    def learn(self):
        '''Construisce gli oggetti problog per la valutazione dell'inferenza'''
        try:
            knowledge_str = ''
            for predicate in self.conoscenza_prob:
                knowledge_str +=predicate+'\n'
            
            knowledge_str = PrologString(knowledge_str)
            self.problog = DefaultEngine()
            self.knowledge_database = self.problog.prepare(knowledge_str) 
            
        except Exception as e: 
            print(e)


    def get_used_card_evidence(self, prolog):
        '''construisce la lista contenente le stringhe delle evidenze per il DTProblog'''
        ret_list = []
        for card in prolog.uscite:
            ret_list.append('evidence(not '+str(card)+').\n')

        return ret_list

    def get_utility(self, prolog):
        '''constuisce la lista delle utility per il DTProblog'''
        vs_score, utility = prolog.get_utility()
        ret_list = []
        for i in range(len(vs_score)):
            ret_list.append(f'utility(vinco({self.punteggio},{vs_score[i]}), {utility[i]}).\n')
            ret_list.append(f'utility(perdo({self.punteggio},{vs_score[i]}), {-1*utility[i]}).\n')
        ret_list.append(f'utility(sballo({self.punteggio}), {-1*prolog.get_winnable_bet()}).\n')
       
        vincita,_ = prolog.get_gain()
        prob_di_migliorare = self.query('prob_di_migliorare',self.punteggio,evidence = self.get_used_card(prolog))
        util = 0
        for i in range(len(vincita)):
            util += prob_di_migliorare*vincita[i]
        ret_list.append(f'utility(miglioro({self.punteggio}), {util}).\n')

        '''
        prob_di_migliorare = self.query('prob_di_migliorare',self.punteggio,evidence = self.get_used_card(prolog))
        for i in range(len(vincita)):
            ret_list.append(f'utility(miglioro({self.punteggio}), {prob_di_migliorare*vincita[i]}).\n')
        '''
        return ret_list

    def decidi(self, prolog):
        '''prende la decisione'''
        temp = self.conoscenza
        evidence = self.get_used_card_evidence(prolog)
        for ev in evidence:
            temp += ev
        utilities = self.get_utility(prolog)
        for ut in utilities:
            temp += ut

        program = PrologString(temp)
        decisions, _, _ = dtproblog(program)

        for _, value in decisions.items():
            if value == 1:
                return True
            print('STO\n')
            return False

    def eval_query(self, term, *args, **kwargs):      
        try:   
            if args:
                t = '\''+term+'\''
                termine = f'Term({t},'
                for termine_arg in args:
                    if isinstance(termine_arg, str):
                        termine+= 'Term(\''+termine_arg+'\')'+','
                    elif isinstance(termine_arg, int) or isinstance(termine_arg, float):
                        termine+= 'Constant('+str(termine_arg)+')'+','
                termine = termine[:-1]+')'

                query_term = eval(termine)
            else:
                query_term = Term(term) 

            evidenze = []
            if kwargs:
                for i in kwargs['evidence']:
                    # Term(Constant(1),Term('spade'))
                    i = i.replace('card(', '').replace(' ', '').replace(')', '').split(',')
                    term_str = f'Term(\'card\',Constant({i[0]}), Term(\'{i[1]}\'))'
                    tupla = (eval(term_str),False)
                    evidenze.append(tupla)

            lf = self.problog.ground_all(self.knowledge_database, queries= [query_term], evidence=evidenze)
            return get_evaluatable().create_from(lf).evaluate()
        except Exception as e:
            print(e)
            print("QUESTA SOPRA è L'ECCEZIONE")
            return None

    def query(self, term, *args, **kwargs):
        # print(ai.query('prob_di_sballare', 7, evidence=['card(2,bastoni)']))
        query_result = self.eval_query(term, *args, **kwargs)
        if len(query_result) > 1:
            res = []
            for prob_res in query_result.values():
                res.append(prob_res)
        else:
            for prob_res in query_result.values():
                res = prob_res
        
        return res

    def get_used_card(self, prolog):
        '''ritorna una lista di stringhe contenenti le carte uscite'''
        uscite = []
        for card in prolog.uscite:
            uscite.append(str(card))

        return uscite
        

