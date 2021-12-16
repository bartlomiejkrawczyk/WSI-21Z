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

# Założenia

- Atrybuty nominalne - każdy atrybut może przyjmować jedną z kilku dozwolonych wartości
- Należy losowo podzielić zbiór danych na trenujący i testujący w stosunku 3:2

# Dokładność

Statystyki dokładności drzew wygenerowanych algorytmem ID3 dla 25 różnych zbiorów trenujących + testowych:

name             | min                 | mean                | max                 | stdev
-----------------|---------------------|---------------------|---------------------|---------------------
Agaricus Lepiota | 100.0 %             | 100.0 %             | 100.0 %             | 0.0 %
Breast Cancer    | 55.65217391304348 % | 64.38260869565218 % | 71.30434782608695 % | 4.173913043478261 %
Car              | 88.8728323699422 %  | 91.58381502890174 % | 93.64161849710982 % | 1.1749422881242075 %
Tic-Tac-Toe      | 78.38541666666666 % | 83.33333333333333 % | 86.97916666666666 % | 2.3158544395753635 %

# Macierze Pomyłek

## Zbiór Breast Cancer

Przykładowa macierz pomyłek:

expected / predicted | no-recurrence-events | recurrence-events
---------------------|----------------------|------------------
no-recurrence-events | 62                   | 14
recurrence-events    | 24                   | 15

## Zbiór Mushroom

Przykładowa macierz pomyłek:

expected / predicted | p    | e
---------------------|------|-----
p                    | 1562 | 0
e                    | 0    | 1688

# Wnioski

- Z wyników wychodzi, że algorytm radzi sobie lepiej dla większych zbiorów
    - dla zbioru mushroom (4874 danych trenujących) dokładność dla danych testowych wyniosła aż 100 % we wszystkich 25 testach
- Dla mniejszych zbiorów algorytm nie radzi sobie, aż tak dobrze

- wyszło mi, że w głównej mierze wynik zależy od:
    - ilości dostępnych atrybutów
    - dobranych par trenujących
