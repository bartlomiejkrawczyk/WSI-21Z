# Wprowadzenie do sztucznej inteligencji - ćwiczenie 1

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie na drugie spotkanie:

1. Zaimplementować metodę najszybszego wzrostu. Gradient wyliczamy numerycznie.

2. Narysować zachowanie algorytmu (kolejne kroki algorytmu jako strzałki na tle poziomic funkcji celu).

    Uwaga: w praktycznych zadaniach optymalizacji nie da się narysować funkcji celu ponieważ zadania mają wiele wymiarów (np. 100), oraz koszt wyznaczenia oceny jednego punktu jest duży.

Zastosować metodę do znalezienia optimum funkcji booth, po czym do znalezienia optimum funkcji o numerach od 1 do 3 z CEC 2017.


### Pytania:
1. ### Jak wartość parametru beta wpływa na szybkość dojścia do optimum i zachowanie algorytmu?

    Wartość parametru beta wpływa na wielkość wykonanego kroku w kierunku optimum.

2. ### Zalety/wady algorytmu?

- Nie modyfikujemy wielkości kroku - dla stosunkowo dużych wartości gradientu wykonujemy wielkie skoki, a dla małych wartości małe, nie zależnie od wartości parametru beta

3. ### Wnioski
