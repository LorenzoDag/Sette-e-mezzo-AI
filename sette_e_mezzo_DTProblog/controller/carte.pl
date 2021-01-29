/**
crea il mazzo di carte:

create_deck(-Deck).

- Deck: mazzo di carte NAPOLETANE mischiato
*/

create_deck(Deck):-
	setof(card(Numero, Seme), (member(Seme, [bastoni, spade, denari, coppe]), between(1, 10, Numero)), Deck_non_shuffled),
	random_permutation(Deck_non_shuffled, Deck).

/**
pesca la prima carta:

draw_card(+Deck, -First, -New).

+ Deck: mazzo di carte da cui pescare una carta
- First: la prima carta del mazzo
- New: il restante mazzo (nuovo mazzo di carte)
*/

draw_card([First|New], First, New).
draw_card([], _,_):- fail.