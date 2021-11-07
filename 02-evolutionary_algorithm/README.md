# Wprowadzenie do sztucznej inteligencji - ćwiczenie 2

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie na trzecie spotkanie:

Zaimplementować klasyczny algorytm ewolucyjny bez krzyżowania, z selekcją turniejową i sukcesją elitarną. Dostępny budżet to 10000 ewaluacji funkcji celu. Optymalizujemy funkcję numer 4 z CEC 2017.

## Badanie Wpływu:

Badania wykonane dla domyślnych parametrów:
- siła mutacji = 1.0
- rozmiar elity = 5
- wielkość populacji = 50

1. Siły mutacji

```
Type            =       Value   Min                     Average                 Std                     Max
mutation_factor =       0.1     400.0000005120068       400.5792188324409       1.230289124210591       407.6495091585116
mutation_factor =       1.0     400.0000001223982       400.1358854527604       0.307606893775548       401.87286240054425
mutation_factor =       2.0     400.0000130851394       400.1757510075227       0.3537591172708558      401.7571360260616
mutation_factor =       3.0     400.0000054581793       400.05701696290384      0.15937813418845742     400.88040794897023
mutation_factor =       4.0     400.0000134135683       400.03424737467395      0.0547248871163359      400.1996237163419
mutation_factor =       5.0     400.00001029007535      400.0230204049806       0.05164635876409938     400.27102590326194
mutation_factor =       10.0    400.00009544850525      400.00671611143144      0.01454985361643587     400.0943454089787
mutation_factor =       20.0    400.00004445317114      400.0044048631134       0.005830952849868928    400.0349719848956
mutation_factor =       30.0    400.0000027655312       400.01225100927763      0.026028299607465555    400.1803902500154
mutation_factor =       40.0    400.0002697092126       400.01666596705         0.023830034484171023    400.1357158537837
mutation_factor =       50.0    400.00026711184154      400.0431186131918       0.0732140139440056      400.33969538122955
mutation_factor =       100.0   400.0015983165405       400.1102677410006       0.13983371162310448     400.58593345764547
```

2. Rozmiaru elity

```
Type            =       Value   Min                     Average                 Std                     Max
elite_count     =       1       400.0000064935315       400.4936393406787       0.8278021744385912      403.89464137238434
elite_count     =       5       400.00000628476363      400.140452118809        0.33210272029230503     402.0266443288437
elite_count     =       10      400.00001003244205      400.26849911401933      0.7041828752702919      404.42376070923393
elite_count     =       20      400.00000044769666      400.18800361722606      0.32156644799043        401.26923173059214
elite_count     =       30      400.0000008569616       400.2256029701033       0.5661691239958179      403.55126709147294
elite_count     =       40      400.00000411652303      400.2094316369426       0.4706948265514817      403.02205798580906
elite_count     =       50      400.000003657085        400.19096812309016      0.2871070578509613      401.5270798566147
```

3. Liczby osobników w populacji

```
Type            =       Value   Min                     Average                 Std                     Max
population_size =       10      400.00000069672285      401.9960238151925       5.074888608881833       426.22286962448266
population_size =       20      400.00000025286147      400.4604579601487       0.8536179212219408      404.26101607424886
population_size =       50      400.0000030251086       400.1703877220345       0.2635434180603956      401.2375359711565
population_size =       100     400.0000028006708       400.0818491263959       0.11374274726670854     400.48036432161365
population_size =       200     400.00000911179586      400.0396700599561       0.08253155918267023     400.34221244343524
population_size =       1000    400.0000881023137       400.01003726023885      0.013208707352495467    400.05849633406876
```

## Wnioski:

## - Wpływ siły mutacji:

Im większa siła mutacji tym algorytm ma większe szanse na eksplorację terenu i znalezienie optimum globalnego,
jednak im mniejsza siła mutacji tym algorytm ma większe szansę na ekploatację dotychczas znalezionego minimum.

Można to też zaobserwować w wynikach. Najlepszą wartość minimalną znalazł algorytm o sile mutacji 0.1, ponieważ
szczęśliwym trafem pewien punkt znalazł minimum lokalne i algorytm mógł wyeksploatować je. Lecz był to jedynie
szczęśliwy traf algorytm o tym współczynniku ma też najgorsze odchylenie standardowe, oraz uzyskał najgorszą średnią.

Im bardziej będziemy zwiększali siłę mutacji tym częściej będziemy uzywkiwali zadowalające nas wyniki, jednak
tutaj też nie możemy przesadzać, ponieważ przy dużym współczynniku szybciej wyjdziemy poza zakres w którym podejrzewamy,
że znajduje się minimum.

## - Wpływ rozmiaru elity:

Wpływ wielkości elity wydaje się nie mieć większego wpływu na wyniki algorytmu.

Może to być spowodowane tym, że przy większych elitach wybieramy jedynie najlepsze osobniki z połączonych zbiorów,
a nie połączonych zbiorów niewielkiej poprzedniej populacji i zmutowanej populacji. Przez to wyniki wydają się być zbliżone.


## - Wpływ wielkości populacji:
Im większa liczba osobników w populacji tym lepsze jest początkowe rozrzucenie po przestrzeni i znalezienie potencjalnego minimum.
Im większa liczba osobników w populacji tym więcej potencjalnych minimów można eksploatować.

Jednak im większa liczba osobników tym mniej możemy wykonać iteracji algorytmu przy ograniczonym budżecie wykonywania funkcji.

Z wyników wynika, że średnio dla danej funkcji lepiej wybierać jest większe populacje, jednak przy mniejszych populacjach jest
więcej czasu na eksploatację i przez to w kolumnie z minimami to właśnie ta z populacją 20 ma znalazła najmniejsze minimum.




