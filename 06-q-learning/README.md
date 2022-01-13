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
1000     | 0.0  | 1.432  | 9.1  | 2.512588306905849
5000     | 0.0  | 4.016  | 14.0 | 3.969958018249899
10000    | 0.0  | 5.52   | 33.5 | 7.2348692685724
25000    | 0.0  | 8.74   | 55.3 | 14.912271233227127
50000    | 0.0  | 23.504 | 86.8 | 25.855696986673298
100000   | 20.4 | 68.212 | 89.1 | 20.47008630498009
250000   | 59.8 | 74.416 | 87.8 | 7.101213511318564

reward_2
episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 3.332  | 15.3 | 4.894275567776433
5000     | 0.0  | 7.3679 | 21.4 | 5.8264998069166705
10000    | 0.0  | 8.632  | 24.9 | 6.78685739745085
25000    | 0.0  | 20.088 | 51.4 | 17.199184089175084
50000    | 0.0  | 42.084 | 82.4 | 23.027242561800577
100000   | 21.2 | 63.908 | 88.5 | 18.41353487700465
250000   | 55.2 | 74.328 | 86.7 | 9.081782130543909

reward_3
episodes | min  | avg    | max  | stdev
---------|------|--------|------|-------------------
1000     | 0.0  | 4.064  | 19.5 | 5.486109732770572
5000     | 0.0  | 5.672  | 17.3 | 4.2845186427415625
10000    | 0.0  | 7.42   | 29.5 | 7.800747827398772
25000    | 0.7  | 14.848 | 46.9 | 14.352761639024969
50000    | 1.9  | 35.172 | 65.3 | 18.047172447043703
100000   | 19.1 | 55.452 | 85.1 | 20.457743440239607
250000   | 26.5 | 69.252 | 86.2 | 14.081048729882776

