/*
 * predicato per il calcolo della perdita in caso il mazziere sballi
 *
 * get_perdita_totale(-Perdita)
 *
 * se il mazziere sblla perde con tutti meno che con quelli
 * che hanno già sballato
 *
 */

get_perdita_totale(Perdita):-
    findall(Puntata,(giocatore(Nome,_,_,Puntata,Punteggio), \+Nome = mazziere, Punteggio =< 7.5),Puntate),
    list_sum(Puntate, Perdita).

/*
 * predicato per il calcolo della vincita in caso di miglioramento,
 * quindi vincendo contro il giocatore con il minimo punteggio più alto
 * del mazziere
 *
 * get_vincita_miglioramento(-Vincita)
 *
 */

get_vincita_miglioramento(Vincita):-
    min_score(Minimo),
    findall(Puntata, (giocatore(Nome,_,_,Puntata,Punteggio),\+Nome=mazziere,Punteggio=Minimo), Puntate),
    list_sum(Puntate, Vincita), !.


/*
 * predicato per la somma di elementi in una lista
 *
 * list_sum(+Lista, -Risultato)
 *
 */

list_sum([Risultato], Risultato):- !.
list_sum([Primo|[Secondo|Resto]], Somma):-
    S is Primo+Secondo,
    list_sum([S|Resto], Somma).

/*
 * predicati per il calcolo del minimo punteggio maggiore di quello
 * del mazziere
 *
 * min_score(-Min_score)
 *
 */
min_score(Min_score):-
    giocatore(mazziere, _, _, _, P_m),
    findall(Punteggio, (giocatore(Nome,_,_,_,Punteggio), \+Nome = mazziere, Punteggio>P_m, Punteggio=<7.5), Players),
    find_min(Players, Min_score).

find_min([Min_score], Min_score):- !.
find_min([Score1|[Score2|Others]], Min_score):-
    Score1 =< Score2,
    find_min([Score1|Others], Min_score);

    find_min([Score2|Others], Min_score).

/*
 * predicati per il calcolo del punteggio massimo in gioco da battere
 *
 * max_score(-Max_score)
 *
 */

max_score(Max_score):-
    giocatore(mazziere,_,_,_,P_m),
    findall(Punteggio, (giocatore(Nome,_,_,_,Punteggio), \+Nome = mazziere, Punteggio=<7.5, Punteggio>P_m), Players),
    find_max(Players, Max_score), !.

find_max([Max_score], Max_score).
find_max([Score1|[Score2|Others]], Max_score):-
    Score1 >= Score2,
    find_max([Score1|Others], Max_score);

    find_max([Score2|Others], Max_score).
