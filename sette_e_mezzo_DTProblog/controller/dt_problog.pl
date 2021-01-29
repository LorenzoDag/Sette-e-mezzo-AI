1/40::card(1,denari);1/40::card(2,denari);1/40::card(3,denari);1/40::card(4,denari);1/40::card(5,denari);1/40::card(6,denari);1/40::card(7,denari);1/40::card(8,denari);1/40::card(9,denari);1/40::card(10,denari);1/40::card(1,coppe);1/40::card(2,coppe);1/40::card(3,coppe);1/40::card(4,coppe);1/40::card(5,coppe);1/40::card(6,coppe);1/40::card(7,coppe);1/40::card(8,coppe);1/40::card(9,coppe);1/40::card(10,coppe);1/40::card(1,spade);1/40::card(2,spade);1/40::card(3,spade);1/40::card(4,spade);1/40::card(5,spade);1/40::card(6,spade);1/40::card(7,spade);1/40::card(8,spade);1/40::card(9,spade);1/40::card(10,spade);1/40::card(1,bastoni);1/40::card(2,bastoni);1/40::card(3,bastoni);1/40::card(4,bastoni);1/40::card(5,bastoni);1/40::card(6,bastoni);1/40::card(7,bastoni);1/40::card(8,bastoni);1/40::card(9,bastoni);1/40::card(10,bastoni).

?::pescare.

valore(Punteggio,Numero, Val):-
card(10,denari),
Val = abs(floor(7.5-Punteggio)); 
card(Numero,_),
Numero < 8, 
Val = Numero;
Val = 0.5.

vinco(Mio,Suo):-   
Suo > 7.5 ;
not pescare,
Mio >= Suo;
pescare,
valore(Mio, V, N),
P is Mio+N,
P >= Suo,
not sballo(Mio).


perdo(Mio, Suo):-
sballo(Mio);
not pescare,
Mio < Suo.


sballo(Mio):-
pescare, 
valore(Mio, V, N),
P is Mio+N,
P > 7.5.

miglioro(Mio):-
pescare,
valore(Mio, V, N),
P is Mio+N,
P =< 7.5.
