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

# Wyniki

reward_default
episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 2.368  | 16.9 | 4.930662565348934
5000     | 0.0  | 37.864 | 77.7 | 21.67484871150585
10000    | 0.0  | 58.944 | 88.0 | 21.20599522147766
25000    | 0.0  | 64.976 | 82.1 | 17.386711400760447
50000    | 0.0  | 61.964 | 82.6 | 18.268412629454154
100000   | 46.0 | 70.712 | 82.3 | 8.58007964221001
250000   | 0.0  | 61.368 | 84.5 | 25.30333838317255

reward_2
episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 14.824 | 77.4 | 22.212257877127215
5000     | 59.7 | 80.868 | 89.3 | 9.415887283380856
10000    | 58.7 | 81.016 | 89.3 | 7.6188188060879884
25000    | 54.8 | 82.024 | 88.9 | 7.956825162504621
50000    | 64.0 | 84.316 | 89.9 | 6.17047269934268
100000   | 73.1 | 83.84  | 90.0 | 4.7635770873017975
250000   | 78.3 | 83.656 | 89.0 | 3.698770065846215

reward_3
episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 17.716 | 73.4 | 20.182370194470884
5000     | 37.9 | 68.628 | 85.5 | 16.61203178422194
10000    | 34.8 | 69.864 | 85.5 | 11.884229045251526
25000    | 59.3 | 72.116 | 83.6 | 8.558070265349933
50000    | 52.7 | 73.244 | 89.2 | 9.350003565061709
100000   | 49.8 | 70.628 | 89.2 | 10.983795640245074
250000   | 55.7 | 73.164 | 84.7 | 8.000514566784647

