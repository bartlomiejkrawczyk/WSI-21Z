# Wprowadzenie do sztucznej inteligencji - ćwiczenie 6

## Student

```
Bartłomiej Krawczyk
310774
```

## Zadanie:

Proszę zaimplementować algorytm Q-Learning i użyć go do wyznaczenia polityki decyzyjnej dla problemu FrozenLake8x8-v0 (w wersji domyślnej, czyli z włączonym poślizgiem). W problemie chodzi o to, aby agent przedostał się przez zamarznięte jezioro z pozycji 'S' do pozycji 'G' unikając punktów 'H'. Symulator dla tego problemu można pobrać z podanej strony lub napisać własny o takiej samej funkcjonalności.
Oprócz zbadania domyślnego sposobu nagradzania (1 za dojście do celu, 0 w przeciwnym przypadku) proszę zaproponować własny system nagród i kar, po czym porównać osiągane wyniki z wynikami systemu domyślnego.

Za wynik uznajemy procent dojść do celu w 1000 prób. W każdej próbie można wykonać maksymalnie 200 akcji.

# Założenia

```python
LEARNING_RATE = 0.05
EPSILON = 0.1
GAMMA = 0.95
```

# Wyniki

## reward_default

- Dojście do celu +1
- Wpadnięcie do dziury 0

episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 2.2    | 7.9  | 2.13834047803431
5000     | 8.0  | 50.284 | 81.6 | 24.921922745513303
10000    | 49.8 | 67.54  | 87.8 | 11.407271073018881
25000    | 51.7 | 68.548 | 83.6 | 10.248460046920869
50000    | 50.0 | 67.16  | 83.1 | 10.603222780519767
100000   | 26.6 | 66.172 | 83.1 | 14.147747759508107
250000   | 54.1 | 69.704 | 86.2 | 9.506553879648852

## reward_2

- Dojście do celu +1
- Wpadnięcie do dziury -1

episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 53.1 | 74.164 | 88.3 | 10.363834554192124
5000     | 70.5 | 83.068 | 89.1 | 5.4933838994436455
10000    | 65.4 | 83.72  | 90.4 | 5.981708228703011
25000    | 64.2 | 83.188 | 88.9 | 5.700096490411369
50000    | 51.1 | 83.392 | 92.2 | 7.96837080797156
100000   | 70.3 | 84.068 | 89.3 | 4.705911176382316
250000   | 60.0 | 83.628 | 89.3 | 6.193916370116728

## reward_3

- Dojście do celu +10
- Wpadnięcie do dziury -1

episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 31.0 | 62.804 | 84.2 | 16.17032982553747
5000     | 54.0 | 73.072 | 84.9 | 8.007471511032682
10000    | 27.6 | 73.936 | 89.2 | 12.670499858595425
25000    | 52.9 | 72.1   | 83.2 | 9.019053904558577
50000    | 62.2 | 73.344 | 82.7 | 6.110583714616252
100000   | 57.7 | 74.26  | 85.8 | 6.994402523923445
250000   | 49.9 | 71.528 | 88.3 | 10.196139792424713

# Wnioski

- Z wyników wyszło mi, że najlepszą funkcją nagrody z testowanych funkcji nagrody dla tego algorytmu jest:
    - 1 dla dojścia do celu i -1 dla wpadnięcia w dziurę
- Wynik zależy w dużym stopniu od dobranych parametrów
- Dużą różnicę wprowadza w przypadku gdy jest kilka maksimów - losowanie wybranej ścieżki