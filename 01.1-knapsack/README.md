# Wprowadzenie do sztucznej inteligencji - ćwiczenie 1

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Zadanie na pierwsze spotkanie:

Mamy problem plecakowy jak na wykładzie:

```python
w = [8, 3, 5, 2] # waga przedmiotów
W = 9 # maksymalna waga plecaka
p = [16, 8, 9, 6] # wartość przedmiotów
```

1. Znaleźć rozwiązanie optymalne przez przegląd wyczerpujący
2. Rozwiązać problem przy użyciu heurystyki:
   - do plecaka pakujemy przedmioty według kolejności wynikającej ze stosunku p/w

## Pytania

- Czy uzyskano takie same rozwiązania? Jakie wnioski można z tego wyciągnąć?
- Jakie wnioski można z tego wyciągnąć?
- Jak dużą instancję problemu (liczba przedmiotów) da się rozwiązać w około minutę metodą zachłanną?
- Jak bardzo wydłuży obliczenia dodanie jeszcze jednego przedmiotu?

## Rozwiązanie

### 1. Przegląd wyczerpujący

W tej metodzie przechodzimy po wszystkich kombinacjach przedmiotów, można to osiągnąć przechodząc przez wszystkie wartości liczb binarnych od 0 do 2 ^ n. Dla 1 przedmiot dodajemy do plecaka, a dla 0 omijamy go. Cały czas śledzimy maksymalną wartość spełniającą warunki zadania i na koniec je zwracamy.

### 2. Rozwiązanie wykorzystujące heurystykę

W tej metodzie rozpoczynamy od stworzenia listy złożonej z liczb odpowiadających wartości/wagę poszczególnych przedmiotów. Sortujemy 4 listy wartość/wagę, wagę, wartość oraz indeksy w pierwszej kolejności biorąc pod uwagę wartość/wagę i kolejno dodajemy przedmioty do plecaka pod warunkiem, że suma wag w plecaku nie będzie przekraczała maksymalnej wagi zadanej.

### Odpowiedzi na pytania

- ### Czy uzyskano takie same rozwiązania?

  Uzyskane rozwiązania różnią się.

  W przeglądzie wyczerpującym otrzymujemy wartość: 17 oraz wybieramy przedmioty 2 i 3.

  W metodzie wykorzystującej heurystykę otrzymujemy wartość: 14 oraz wybieramy przedmioty 2 i 4.

- ### Jakie wnioski można z tego wyciągnąć?

  Oczywistym jest, że jeśli przejdziemy po wszystkich możliwych ustawieniach przedmiotów otrzymamy najlepsze możliwe dopasowanie.

  Wykorzystując heurystykę możemy uzyskać rozwiązanie najlepsze, ale nie jest to gwarantowane, tak jak okazało się w przykładzie.

  Jednak wykorzystanie heurystyki wykonujemy mniej obliczeń dla większych zbiorów przedmiotów. Złożoność obliczeniowa przeglądu zachłannego rośnie wykładniczo (2 ^ n), a złożoność obliczeniowa metody wykorzystującej heurystykę zależy głównie od wydajności użytej metody sortującej od ok. (n log n) do (n ^ 2).

- ### Jak dużą instancję problemu (liczba przedmiotów) da się rozwiązać w około minutę metodą zachłanną?

Wykonanie dla 24 przedmiotów zajeło: 45.128666162490845 sekund

- ### Jak bardzo wydłuży obliczenia dodanie jeszcze jednego przedmiotu?

Dodanie dodatkowego przedmiotu wydłuży obliczenia dwukrotnie, ponieważ będziemy brali pod uwagę 2^(n + 1) kombinacji przedmiotów, gdzie poprzednio braliśmy jedynie 2^n kombinacji.
