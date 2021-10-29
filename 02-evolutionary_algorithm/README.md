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
mutation_factor =       0.1     400.02997657684944      402.5728873635133       1.6103832873002337      404.160712691783
mutation_factor =       1.0     400.00000122588267      401.53609248580574      1.563701620779842       404.160712691783
mutation_factor =       10.0    400.00000610461683      400.3114934849956       0.8428783951557355      404.160712691783
mutation_factor =       50.0    400.00000276036553      400.16286233607565      0.5614080128369762      404.160712691783
```

2. Rozmiaru elity

```
Type            =       Value   Min                     Average                 Std                     Max
elite_count     =       1       400.0000071879555       401.77051736125975      1.7621963005304326      404.160712691783
elite_count     =       5       400.00000122588267      400.49235088511716      1.0241601903480595      403.9878778491874
elite_count     =       10      400.00000276036553      401.1746335064156       1.5703375805472009      404.04500508273964
```

3. Liczby osobników w populacji

```
Type            =       Value   Min                     Average                 Std                     Max
population_size =       10      400.0004258864333       401.5973622979902       1.7275766829382513      404.160712691783
population_size =       50      400.0000173759129       401.36886909229185      1.6987320444800034      404.00649951859884
population_size =       100     400.00000122588267      400.4712703625104       0.9272511085647951      403.5324974740208
```
