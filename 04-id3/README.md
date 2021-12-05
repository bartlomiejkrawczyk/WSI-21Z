# Wprowadzenie do sztucznej inteligencji - ćwiczenie 4

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie:

- Zaimplementować klasyfikator ID3 (drzewo decyzyjne).
- Atrybuty nominalne, testy tożsamościowe.
- Podać dokładność i macierz pomyłek na zbiorach:
    - Breast cancer
    - mushroom
- Sformułować i spisać w kilku zdaniach wnioski.

Poniżej kilka wskazówek ogólnych do tego ćwiczenia:
- Atrybuty nominalne - każdy atrybut może przyjmować jedną z kilku dozwolonych wartości, zakładamy, że wartość atrybutu to napis, np. "kot", "a", "20-34", ">40".
- Testy tożsamościowe - jeżeli atrybut testowany w danym węźle ma np. 3 dozwolone wartości, np. a, b, c, to z węzła tego wychodzą 3 krawędzie oznaczone: a, b, c.
- Na tym ćwiczeniu klasyfikator trenuje się na zbiorze trenującym, a ocenia jego jakość na zbiorze testującym. Należy losowo podzielić zbiór danych na trenujący i testujący w stosunku 3:2.
- Jeżeli zbiór danych zawiera numery lub identyfikatory wierszy to należy je wyrzucić - nie chcemy uczyć się identyfikatorów wierszy.
- Brakujące wartości atrybutów traktujemy jako wartość, np. jeżeli symbol ‘?’ oznacza brakującą wartość, a symbole ‘a’, ‘b’ wartości normalne, to z naszego punktu widzenia mamy 3 wartości normalne (fachowo: 3 wartości atrybutu): ‘a’, ‘b’, ‘?’.
- Tak na prawdę to nie musimy rozumieć dziedziny problemu - na wejściu mamy napisy, na wyjściu napisy, nie ważne czy klasyfikujemy sekwencje DNA, grzyby, czy samochody.
- Nazwa pliku ze zbiorem danych jest parametrem algorytmu klasyfikacji, kod klasyfikatora powinien być w stanie obsłużyć inny zbiór danych o tym samym rozkładzie kolumn (czyli nie należy wpisywać wartości atrybutów „na sztywno” w kodzie).
- W repozytorium ze zbiorami danych zwykle w plikach „.names” jest napisane, który atrybut to klasa (czyli wartości której kolumny mamy się nauczyć przewidywać).


name             | min               | mean               | max                | stdev
-----------------|-------------------|--------------------|--------------------|---------------------
Agaricus Lepiota | 1.0               | 1.0                | 1.0                | 0.0
Breast Cancer    | 0.591304347826087 | 0.6650434782608695 | 0.7391304347826086 | 0.037327211668417966