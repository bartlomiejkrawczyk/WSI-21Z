# Wprowadzenie do sztucznej inteligencji - ćwiczenie 2

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie na trzecie spotkanie:

Zaimplementować klasyczny algorytm ewolucyjny bez krzyżowania, z selekcją turniejową i sukcesją elitarną. Dostępny budżet to 10000 ewaluacji funkcji celu. Optymalizujemy funkcję numer 4 z CEC 2017.

## Działanie Algorytmu:

![Gif](./animation.gif)

## Badanie Wpływu:

Badania wykonane dla domyślnych parametrów:

- siła mutacji = 1.0
- rozmiar elity = 5
- wielkość populacji = 50

## 1. Siły mutacji

| Type            | Value | Min                | Average            | Std                    | Max                |
|-----------------|-------|--------------------|--------------------|------------------------|--------------------|
| mutation_factor | 0.1   | 400.00000004492546 | 400.5406481661391  | 0.854308724167775      | 403.2307143256784  |
| mutation_factor | 1.0   | 400.00000003812943 | 400.00000225744736 | 2.1014582506487206e-06 | 400.00000744803475 |
| mutation_factor | 2.0   | 400.0000000044616  | 400.00000810964883 | 1.0631792806760805e-05 | 400.00005227399447 |
| mutation_factor | 3.0   | 400.00000008796025 | 400.0000118467875  | 1.0784572960930645e-05 | 400.00003540824616 |
| mutation_factor | 4.0   | 400.00000099786166 | 400.0000215355624  | 2.19984540393364e-05   | 400.00007377099524 |
| mutation_factor | 5.0   | 400.0000013398108  | 400.0000336794064  | 3.582937259524924e-05  | 400.000139368603   |
| mutation_factor | 10.0  | 400.00000435619546 | 400.00021113418234 | 0.00017972166447058607 | 400.00064501196397 |
| mutation_factor | 20.0  | 400.0000776106671  | 400.0009311557691  | 0.0007044010107806523  | 400.00248920395796 |
| mutation_factor | 30.0  | 400.00013640194106 | 400.00194165250724 | 0.0020606623241182765  | 400.01009225341835 |
| mutation_factor | 40.0  | 400.00030695179146 | 400.0029615578364  | 0.0024981516338288923  | 400.0104253469711  |
| mutation_factor | 50.0  | 400.0003258418493  | 400.00438075539245 | 0.003637061791620829   | 400.01297088896195 |
| mutation_factor | 100.0 | 400.00115551722143 | 400.0157379634939  | 0.009687836379298195   | 400.04061264552513 |

## - Wpływ siły mutacji:

Przy bardzo małej sile mutacji jesteśmy w stanie znaleźć minimum jedynie gdy się nam poszczęści. Algorytm o takim
współczynniku ma niewielkie szanse na eksplorację. I dlatego też to tutaj osiągamy największe maksimum.

Im większy współczynnik tym bardziej nasz algorytm preferuje eksplorację od eksploatacji znalezionych optimów.
Dlatego też dla wyższej siły mutacji nie znajdujemy dokładnego optimum.

Aby algorytm działał najlepiej dla danej funkcji powinniśmy wybrać pomiędzy eksploracją i eksploatacją wybierając siłę mutacji pomiędzy 1.0 - 2.0

## 2. Rozmiaru elity

| Type        | Value | Min                | Average            | Std                    | Max                |
|-------------|-------|--------------------|--------------------|------------------------|--------------------|
| elite_count | 0     | 400.0000002404315  | 400.00093178205753 | 0.003459150107409316   | 400.0170985701036  |
| elite_count | 1     | 400.0000000999859  | 400.0000048257121  | 4.917104673869166e-06  | 400.00002291680187 |
| elite_count | 2     | 400.0000000728775  | 400.0000032135157  | 3.7006686319222794e-06 | 400.0000141858302  |
| elite_count | 3     | 400.00000015429003 | 400.00000395220286 | 3.1951658740399884e-06 | 400.0000117888886  |
| elite_count | 4     | 400.00000009874077 | 400.0000028883181  | 2.7867237101743585e-06 | 400.0000105361532  |
| elite_count | 5     | 400.00000004589754 | 400.0000024841704  | 2.160633403650698e-06  | 400.00000765794147 |
| elite_count | 10    | 400.000000178131   | 400.00005916104215 | 0.00028577282041542673 | 400.00143084002184 |
| elite_count | 20    | 400.0000001278414  | 400.0000027885444  | 3.4403721044816832e-06 | 400.0000123899245  |
| elite_count | 30    | 400.0000001036102  | 400.00169926618713 | 0.004678001648317394   | 400.0178281879155  |
| elite_count | 40    | 400.00000012414085 | 400.00090955935565 | 0.0031891456497810462  | 400.01328428961796 |
| elite_count | 50    | 400.0000000226477  | 400.00135730202703 | 0.0045081963993773445  | 400.0206889725324  |

## - Wpływ rozmiaru elity:

Wybranie zerowego rozmiaru elity wydaje się być słabym pomysłem, ponieważ jesteśmy w stanie zgubić najmniejszą wartość i tak również wynika z tabeli.

Podobnie gdy wybierzemy wielki rozmiar elity osiągamy wartości odstające od tych wartości mniejszych.

Optymalnym wyborem dla danej funkcji (przy wielkości populacji równej 50) wydaje się być rozmiar elity równy 5, jednak nie ma to większego wpływu na wynik.

## 3. Liczby osobników w populacji

| Type            | Value | Min                | Average            | Std                    | Max                |
|-----------------|-------|--------------------|--------------------|------------------------|--------------------|
| population_size | 5     | 400.0000000692429  | 400.000001100487   | 1.1787788987110282e-06 | 400.0000042188017  |
| population_size | 10    | 400.00000004497804 | 400.0000015001062  | 1.5493200720349807e-06 | 400.0000069554199  |
| population_size | 15    | 400.00000002379255 | 400.0000020135678  | 3.139242133938153e-06  | 400.00001306949173 |
| population_size | 20    | 400.00000003136677 | 400.00000200151436 | 2.426285427870583e-06  | 400.0000104482362  |
| population_size | 50    | 400.0000000751641  | 400.00000285018206 | 3.298924154146688e-06  | 400.0000165153286  |
| population_size | 100   | 400.0000000148837  | 400.00076417911606 | 0.003435714897103905   | 400.01715866018526 |
| population_size | 200   | 400.0000005980138  | 400.0009144067704  | 0.004534426594121134   | 400.0226796299264  |
| population_size | 1000  | 400.00000045087035 | 400.00082624512567 | 0.0023627848837601867  | 400.0112773201329  |

## - Wpływ wielkości populacji:

Im większa liczba osobników w populacji tym lepsze jest początkowe rozrzucenie po przestrzeni i znalezienie potencjalnego minimum.
Im większa liczba osobników w populacji tym więcej potencjalnych minimów można eksploatować.

Jednak im większa liczba osobników tym mniej możemy wykonać iteracji algorytmu przy ograniczonym budżecie wykonywania funkcji.

Z wyników wynika, że średnio dla danej funkcji lepiej wybierać jest mniejsze populacje.

## Wnioski:

- Algorytm całkiem prosty w implementacji
- Dla niewielkich wymiarów działa bardzo dobrze
- Łatwo zwiększyć wymiar działania algorytmu
