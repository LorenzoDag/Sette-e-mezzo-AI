
/**

Il mazzaro da una carta a testa, tutte scoperte tranne la propria.
A turno i giocatori decidono se pescare una carta o restare con il punteggio attuale.

Il punteggio massimo raggiungibile è 7 e mezzo,
le figure valgono mezzo e i numeri valgono il loro valore.
*/


valore(card(Numero, _), Val):-
	(Numero = 8; Numero = 9; Numero = 10) -> Val = 0.5, !; Val = Numero, !.
valore([T|C], Valore):-
	length([T|C],1),
	T = card(10,denari),
	Valore = 0.5;
	member(card(10,denari), [T|C]) ->
	    select(card(10,denari), [T|C], New_list),
	    append(New_list, [card(10,denari)], New_list_matta),
	    score(New_list_matta, Valore, 0), !
	        ;
	    score([T|C], Valore, 0).

/**
valuta il punteggio di un giocatore

score(+Lista, -Punteggio)

+ Lista: le carte pescate dal giocatore
- Punteggio: Il punteggio ottenuto
*/

score([], Punteggio, Punteggio).
score([card(10, denari)], Punteggio, Inizio):-
	Inizio =\= 7.0,
	Punteggio_matta is floor(7.5 - Inizio),
	abs(Punteggio_matta, Punteggio_matta_abs),
	Punteggio is Inizio + Punteggio_matta_abs, !;

	Inizio =:= 7.0,
	Punteggio is 7.5.
score([card(V, _)|C], Punteggio, Begin):-
	valore(card(V,_), X),
	Punteggio_new is Begin + X,
	score(C, Punteggio, Punteggio_new).

/**
giocatore sballa

sballato(+Lista)

+ Lista: calcola il punteggio e torna vero se > 7.5

true se il giocatore sballa
*/

sballato(Nome):-
	giocatore(Nome, Carte, _, _, _),
	sballato(Carte).
sballato([T|C]):-
	valore([T|C], Punteggio),
	Punteggio > 7.5,
	true.

/**
 * puntata
 * punta(+Nome, +Puntata)
 *
 * + Nome: nome UNICO del giocatore
 * + Puntata: Puntata da fare
 *
* torna vero se la puntata � fattibile e sottrae la puntata allo stack
* del giocatore
*/

punta([]).
punta([Nome|Altri]):-
	giocatore(Nome, Carta, Soldi, _, Punteggio),
	nl, nl,tab(1), write(Nome), write(' il tuo punteggio �: '), write(Punteggio),
	nl,
	tab(8),write(Carta), nl,
	tab(1),write('hai '), write(Soldi), write('�'),
	tab(1),write(' quanto vuoi puntare? '), read(Puntata),
	punta(Nome, Puntata),
	punta(Altri).
punta(Nome, Puntata):-
	giocatore(Nome, Lista, Stack, P, Punteggio),
	(Stack >= Puntata) ->
	retract(giocatore(Nome, Lista, Stack, P, Punteggio)), Stack_new is Stack-Puntata, asserta(giocatore(Nome, Lista, Stack_new, Puntata, Punteggio))
	;
	write('La puntata � maggiore della disponibilit�'), punta([Nome]).
/*
 * valuta la vittoria di un giocatore
 * who_win(+Nome1, +Nome2, -Winner)
 *
 * + Nome1, Nome2: nomi UNICI dei giocatori da valutare
 * - Winner : nome UNICO del giocatore vincitore
 */
who_win(Nome1, Nome2, Winner):-
	giocatore(Nome1, _, _, _, _),
	giocatore(Nome2, _, _, _, _),
	sballato(Nome1),\+ sballato(Nome2) , Winner = Nome2;

	giocatore(Nome1, _, _, _, _),
	giocatore(Nome2, _, _, _, _),
	sballato(Nome1), sballato(Nome2) , Winner = Nome1;

	giocatore(Nome1, _, _, _, Punteggio1),
	giocatore(Nome2, _, _, _, Punteggio2),
	\+ sballato(Nome1), \+ sballato(Nome2), Punteggio1 >= Punteggio2, Winner = Nome1;

    giocatore(Nome1, _, _, _, Punteggio1),
	giocatore(Nome2, _, _, _, Punteggio2),
	\+ sballato(Nome1), \+ sballato(Nome2), Punteggio1 < Punteggio2,  Winner = Nome2;

	giocatore(Nome1, _, _, _, _),
	giocatore(Nome2, _, _, _, _),
    \+ sballato(Nome1), sballato(Nome2), Winner = Nome1.

print_winners([]).
print_winners([Nome|Altri]):-
	who_win(mazziere, Nome, Winner),
	nl, tab(5), write('mazziere vs '), write(Nome),write(' vince: '), write(Winner),
	print_winners(Altri).


/*
 * aggiorna il db del vincitore
 * make_win(+Nome)
 *
 * + Nome: giocatore da aggiornare in base all'esito della giocata
 *
 * NOTA : IL MAZZIERE HA DISPONIBILITA' INFINITE
 *
make_win(Nome):-
	giocatore(Nome, Carte, Stack, Puntata, Punteggio),
	retract(giocatore(Nome,Carte,Stack,Puntata, Punteggio)),
	Stack_n is Stack+Puntata+Puntata,
	asserta(giocatore(Nome,[],Stack_n,0, 0)).
*/

/* calcoli la vincita totale del mazziere contro tutti i suoi avversari
 
*/
 
vincita_mazziere(Vincita) :-
    findall(Nome, (giocatore(Nome,_,_,_,_)), Nomi_giocatori),
    calcola_vincita(Nomi_giocatori, 0, Vincita), !.
 
calcola_vincita([],Vincita,Vincita).
 
calcola_vincita([Nome|Altri], Inizio, Vincita) :-
    who_win(mazziere, Nome, Winner),
    Winner = mazziere,
    giocatore(Nome, _, _, Puntata,_),
    Vincita1 is Inizio + Puntata,  
    calcola_vincita(Altri, Vincita1, Vincita);
 
    who_win(mazziere, Nome, Winner),
    \+ Winner = mazziere,
	giocatore(Nome, _, _, Puntata, _),
    Vincita1 is Inizio - Puntata, 
    calcola_vincita(Altri, Vincita1, Vincita).