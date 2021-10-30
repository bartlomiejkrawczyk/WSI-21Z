# Wprowadzenie do sztucznej inteligencji - ćwiczenie 2

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie na trzecie spotkanie:

Zaimplementować klasyczny algorytm ewolucyjny bez krzyżowania, z selekcją turniejową i sukcesją elitarną. Dostępny budżet to 10000 ewaluacji funkcji celu. Optymalizujemy funkcję numer 4 z CEC 2017.

## Badanie Wpływu:

1. Siły mutacji

```
Type            =       Value   Min                     Average                 Std                     Max
mutation_factor =       0.1     400.0000000820065       402.9214001268582       6.8914996112564175      457.1211928941919
mutation_factor =       1.0     400.0000098494303       401.08966260665284      2.9717592948698885      421.22113126179397
mutation_factor =       10.0    400.0000062472993       400.12812399527786      0.4384561422125095      403.90865673313175
mutation_factor =       50.0    400.0000214178407       400.0750699917187       0.35706688092354644     403.58128906123255
```

2. Rozmiaru elity

```
Type            =       Value   Min                     Average                 Std                     Max
elite_count     =       1       400.0000062472993       401.2415345961977       4.473911324299581       441.9881986618225
elite_count     =       5       400.0000000820065       400.4674687320724       1.1544073300534154      410.660758138851
elite_count     =       10      400.0000018223599       401.45168921211047      4.953701853447564       457.1211928941919
```

3. Liczby osobników w populacji

```
Type            =       Value   Min                     Average                 Std                     Max
population_size =       10      400.0000062472993       402.60924046885384      6.477652221776586       457.1211928941919
population_size =       50      400.0000018223599       400.35129940509336      0.7658306716567228      405.714190475637
population_size =       100     400.0000000820065       400.2001526664334       0.47599613749155384     404.94384102192447
```
