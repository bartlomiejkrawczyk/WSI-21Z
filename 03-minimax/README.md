# Wprowadzenie do sztucznej inteligencji - ćwiczenie 3

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie:

Zaimplementować algorytm min-max z przycinaniem alfa-beta. Algorytm ten należy zastosować do gry w proste warcaby (checekers/draughts). Niech funkcja oceny planszy zwraca różnicę pomiędzy stanem planszy gracza a stanem przeciwnika. Za pion przyznajemy 1 punkt, za damkę 10 p.
Przygotowałem dla Państwa kod, który powinien ułatwić wykonanie zadania. Zamiast mojego kodu, osoby chętne mogą napisać własny kod pomocniczy. Nie można używać kodu z Internetu, czy bardziej ogólnie, kodu, którego nie jest się autorem.

Wiem co jest dostępne w Internecie, większość dostępnych implementacji ma cechy szczególne, po których łatwo je rozpoznać.

Zasady gry (w skrócie: wszyscy ruszają się po 1 polu. Pionki tylko w kierunku wroga, damki w dowolnym) z następującymi modyfikacjami:
- bicie nie jest wymagane
- dozwolone jest tylko pojedyncze bicie (bez serii).

Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?

Niech komputer gra z komputerem (bez wizualizacji), zmieniamy parametry jednego z oponentów, badamy jak zmiany te wpłyną na liczbę jego wygranych. Należy zbadać wpływ:
- Głębokości drzewa przeszukiwań
- Alternatywnych funkcji oceny stanu, np.:
    - nagrody jak w wersji podstawowej + nagroda za stopień zwartości grupy (jak wszyscy blisko siebie to OK, no chyba, że da się coś zabrać przeciwnikowi)
    - za każdy pion na własnej połowie planszy otrzymuje się 5 nagrody, na połowie przeciwnika 7, a za każdą damkę 10.
    - za każdy nasz pion otrzymuje się nagrodę w wysokości: (5 + numer wiersza, na którym stoi pion) (im jest bliżej wroga tym lepiej), a za każdą damkę: 10.

## Pytania

### Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?

- gracz sterowany przez AI nie zawsze zachowuje się rozsądnie
- taki gracz stara się uzyskać jak najlepszą ewaluację i do tego dąży:
    - np. w przypadku ewaluacji podstawowej, AI woli zdobyć damkę niż zbić kilka pionków gracza
    - taki algorytm jeśli ma możliwość zbić pionek gracza, często pozostawia to potencjalne zbicie na później, ponieważ nadal będzie mogło uzyskać taką samą lub lepszą ewaluację (chyba, że ustawimy głębokość na 1 wtedy ai przewiduje jedynie ewaluację w kolejnym swoim ruchu)
- ai vs ai bardzo często kończy remisem, ponieważ wpadają one w cykle i nie mogą zakończyć rozgrywki
    - sytuacja ta występuje gdy więcej niż jeden ruch ma tę samą maksymalną wartość ewaluacji i w tym przypadku wybierana jest wartość pierwsza z listy ruchów o takiej wartości ewaluacji - rozgrywka kończy się wtedy remisem pomimo często znaczącej przewagi jednej ze stron
- jednak, jak odpalam grę w wersji ja przeciwko AI, ciężko mi jest wygrać, chyba, że przyjmę taktykę zdobądź jedną damkę, i pozostaw 1 rząd pionów nie ruszony - zablokuj możliwość AI zdobycia damki i przez to ma jedynie ograniczoną liczbę ruchów - i przez to przegrywa


### Porównianie głębokości na planszy 8x8 z 3 rzędami pionów

blue \ white | 1    | 2     | 3     | 4     | 5
-------------|------|-------|-------|-------|------
1            | blue | white | white | white | draw
2            | blue | draw  | white | white | draw
3            | draw | draw  | draw  | white | draw
4            | blue | draw  | blue  | draw  | white
5            | blue | draw  | white | white | draw

- z porównywania głębokości wynika, że im większa jest głębokość tym większa szansa na wygranie danego ai
- można też zauważyć, że białe pionki są w nieco lepszej sytuacji

### Gra na planszy 8x8 z 3 rzędami pionów na starcie vs przeciwnik z ustawioną funkcją ewaluującą podstawową i głębokością 3.

Gracz biały:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_random    | lose | lose | lose | lose | lose
evaluate_basic     | draw | draw | draw | win  | draw
evaluate_version_1 | lose | lose | draw | draw | draw
evaluate_version_2 | lose | draw | draw | win  | draw
evaluate_version_3 | lose | draw | draw | win  | draw

Gracz niebieski:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_random    | lose | lose | lose | lose | lose
evaluate_basic     | lose | lose | draw | win  | lose
evaluate_version_1 | lose | win  | draw | draw | win
evaluate_version_2 | lose | lose | draw | draw | draw
evaluate_version_3 | lose | lose | draw | draw | draw

### Gra na planszy 8x8 z 3 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|------------
evaluate_random    | [1, 3, 21]  | [3, 6, 16]  | [3, 10, 12] | [5, 12, 8]  | [6, 13, 6]
evaluate_basic     | [7, 4, 14]  | [12, 13, 0] | [11, 11, 3] | [19, 6, 0]  | [11, 14, 0]
evaluate_version_1 | [2, 11, 12] | [3, 14, 8]  | [6, 13, 6]  | [7, 16, 2]  | [12, 9, 4]
evaluate_version_2 | [5, 3, 17]  | [8, 16, 1]  | [8, 15, 2]  | [13, 12, 0] | [11, 13, 1]
evaluate_version_3 | [2, 6, 17]  | [10, 11, 4] | [5, 17, 3]  | [11, 10, 4] | [7, 15, 3]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3          | 4           | 5
-------------------|------------|------------|------------|-------------|------------
evaluate_random    | [0, 2, 23] | [2, 2, 21] | [3, 7, 15] | [5, 8, 12]  | [5, 8, 12]
evaluate_basic     | [7, 11, 7] | [7, 8, 10] | [7, 15, 3] | [9, 15, 1]  | [10, 11, 4]
evaluate_version_1 | [1, 5, 19] | [5, 9, 11] | [4, 18, 3] | [6, 15, 4]  | [7, 16, 2]
evaluate_version_2 | [6, 11, 8] | [6, 13, 6] | [9, 14, 2] | [12, 11, 2] | [11, 13, 1]
evaluate_version_3 | [6, 11, 8] | [8, 11, 6] | [8, 11, 6] | [10, 14, 1] | [10, 14, 1]


### Gra na planszy 6x6 z 2 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3           | 4           | 5
-------------------|------------|------------|-------------|-------------|------------
evaluate_random    | [1, 0, 24] | [3, 5, 17] | [3, 9, 13]  | [5, 11, 9]  | [6, 14, 5]
evaluate_basic     | [7, 4, 14] | [8, 14, 3] | [13, 5, 7]  | [15, 9, 1]  | [14, 11, 0]
evaluate_version_1 | [1, 3, 21] | [4, 14, 7] | [13, 6, 6]  | [14, 8, 3]  | [11, 11, 3]
evaluate_version_2 | [5, 8, 12] | [7, 15, 3] | [12, 10, 3] | [14, 10, 1] | [7, 16, 2]
evaluate_version_3 | [2, 8, 15] | [6, 14, 5] | [10, 11, 4] | [12, 12, 1] | [9, 15, 1]

Gracz niebieski:

evaluation \ depth | 1           | 2          | 3           | 4           | 5
-------------------|-------------|------------|-------------|-------------|------------
evaluate_random    | [2, 1, 22]  | [2, 4, 19] | [7, 3, 15]  | [7, 8, 10]  | [8, 10, 7]
evaluate_basic     | [2, 5, 18]  | [4, 13, 8] | [7, 11, 7]  | [11, 14, 0] | [14, 10, 1]
evaluate_version_1 | [3, 4, 18]  | [3, 8, 14] | [7, 13, 5]  | [9, 14, 2]  | [8, 16, 1]
evaluate_version_2 | [3, 10, 12] | [7, 11, 7] | [12, 8, 5]  | [14, 10, 1] | [13, 9, 3]
evaluate_version_3 | [1, 8, 16]  | [5, 13, 7] | [10, 13, 2] | [10, 14, 1] | [11, 13, 1]
