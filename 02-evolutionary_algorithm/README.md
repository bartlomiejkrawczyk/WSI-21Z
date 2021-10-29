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
mutation_factor =       0.1     400.00000394959824      402.7847284699955       8.799281975428135       486.95604223056193
mutation_factor =       1.0     400.0000000122288       401.68741848770674      7.106907564915494       469.6230938335466
mutation_factor =       10.0    400.0000016117719       400.2677060620176       1.1619143122308708      413.9646331791626
mutation_factor =       50.0    400.00002401807575      400.07581173453684      0.30896698706593057     403.4155715529421
```

2. Rozmiaru elity

```
Type            =       Value   Min                     Average                 Std                     Max
elite_count     =       1       400.0000005139107       400.91791048333687      4.188223360665326       466.20183943316874
elite_count     =       5       400.0000000122288       400.80983841675277      3.803125216913047       454.3882269323302
elite_count     =       10      400.0000005129926       401.8839996656028       8.23979867833488        486.95604223056193
```

3. Liczby osobników w populacji

```
Type            =       Value   Min                     Average                 Std                     Max
population_size =       10      400.00001075523835      403.12730174614353      9.709878023088146       486.95604223056193
population_size =       50      400.0000005139107       400.3331061621971       0.8061686601045404      405.7270880734479
population_size =       100     400.0000000122288       400.15134065735185      0.29209220930344054     402.41014278959886
```
