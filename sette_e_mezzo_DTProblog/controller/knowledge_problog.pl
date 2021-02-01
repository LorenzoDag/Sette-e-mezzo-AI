1/40::card(1,denari);1/40::card(2,denari);1/40::card(3,denari);1/40::card(4,denari);1/40::card(5,denari);1/40::card(6,denari);1/40::card(7,denari);1/40::card(8,denari);1/40::card(9,denari);1/40::card(10,denari);
1/40::card(1,coppe);1/40::card(2,coppe);1/40::card(3,coppe);1/40::card(4,coppe);1/40::card(5,coppe);1/40::card(6,coppe);1/40::card(7,coppe);1/40::card(8,coppe);1/40::card(9,coppe);1/40::card(10,coppe);
1/40::card(1,spade);1/40::card(2,spade);1/40::card(3,spade);1/40::card(4,spade);1/40::card(5,spade);1/40::card(6,spade);1/40::card(7,spade);1/40::card(8,spade);1/40::card(9,spade);1/40::card(10,spade);
1/40::card(1,bastoni);1/40::card(2,bastoni);1/40::card(3,bastoni);1/40::card(4,bastoni);1/40::card(5,bastoni);1/40::card(6,bastoni);1/40::card(7,bastoni);1/40::card(8,bastoni);1/40::card(9,bastoni);1/40::card(10,bastoni).


prob_di_sballare(P) :-
    valore(P, N, V),
    P1 is V + P,
    P1 > 7.5.
    
    
valore(Punteggio,Numero, Val):- 
    card(10,denari),
    Val = abs(floor(7.5-Punteggio));

    card(Numero,_),
    Numero < 8,
    Val = Numero;

    Val = 0.5.

prob_di_migliorare(Mio_punteggio):-
    valore(Mio_punteggio, N, Nuovo),
    Nuovo_mio_punteggio is Mio_punteggio + Nuovo,
    Nuovo_mio_punteggio =< 7.5.