# Wprowadzenie do sztucznej inteligencji - ćwiczenie 1_2

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

### 1. Jak wartość parametru beta wpływa na szybkość dojścia do optimum i zachowanie algorytmu?

Wartość parametru beta wpływa na wielkość wykonanego kroku w kierunku optimum.

- Przy małym beta dojście do optimum wymaga większej ilości punktów, lecz zabezpiecza przed przeskoczeniem optimum i wyleceniem poza zakres.
- Przy większym beta dojście do optimum następuje w mniejszej ilości kroków, lecz nie gwarantuje, że algorytm nie wyskoczy poza zakres.

### 2. Zalety/wady algorytmu?

### Zalety:

- Algorytm skaluje się i działa dla różnych wymiarów
- Implementacja jest prosta

### Wady:

- Algorytm nie wybiera najkrótszej trasy do optimum
- Nie modyfikujemy wielkości kroku - dla stosunkowo dużych wartości gradientu wykonujemy wielkie skoki, a dla małych wartości małe, nie zależnie od wartości parametru beta
- Algorytm nie gwarantuje, że w kolejnych krokach będzie zbliżał się od optimum

### 3. Wnioski

Algorytm najszybszego wzrostu jest łatwy w implementacji oraz jest w stanie znaleźć optimum nawet dla dużej ilości wymiarów, jednak należy ustalić odpowiedni współczynnik beta. Gdybyśmy byli w stanie modyfikować współczynnik beta w trakcie działania programu osiągnelibyśmy wynik w mniejszej ilości kroków.
