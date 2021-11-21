# Wprowadzenie do sztucznej inteligencji - ćwiczenie 3

## Student

Imię: Bartłomiej

Nazwisko: Krawczyk

Numer indeksu: 310774

## Pytania

### Czy gracz sterowany przez AI zachowuje się rozsądnie z ludzkiego punktu widzenia? Jeśli nie to co jest nie tak?

- gracz sterowany przez AI nie zawsze zachowuje się tak jak człowiek
- taki gracz stara się uzyskać jak najlepszą ewaluację i do tego dąży:
    - np. w przypadku ewaluacji podstawowej, AI woli zdobyć damkę niż zbić kilka pionków gracza


### Gra na planszy 8x8 z 3 rzędami pionów na starcie vs przeciwnik z ustawioną funkcją ewaluującą podstawową i głębokością 3.

Gracz biały:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_random    | lose | lose | lose | draw | draw
evaluate_default   | draw | draw | draw | win  | draw
evaluate_basic     | draw | draw | draw | win  | draw
evaluate_version_1 | lose | draw | lose | draw | draw
evaluate_version_2 | lose | draw | draw | lose | draw
evaluate_version_3 | draw | draw | draw | win  | draw

Gracz niebieski:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_random    | lose | lose | lose | lose | lose
evaluate_default   | lose | lose | draw | win  | lose
evaluate_basic     | lose | lose | draw | win  | lose
evaluate_version_1 | lose | lose | lose | lose | lose
evaluate_version_2 | lose | lose | draw | draw | draw
evaluate_version_3 | lose | lose | lose | lose | draw

### Gra na planszy 8x8 z 3 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|------------
evaluate_random    | [2, 7, 21]  | [8, 5, 17]  | [1, 14, 15] | [8, 2, 20]  | [4, 16, 10]
evaluate_default   | [9, 5, 16]  | [13, 15, 2] | [22, 6, 2]  | [26, 4, 0]  | [15, 15, 0]
evaluate_basic     | [9, 5, 16]  | [14, 14, 2] | [22, 6, 2]  | [25, 5, 0]  | [14, 16, 0]
evaluate_version_1 | [6, 6, 18]  | [9, 10, 11] | [6, 8, 16]  | [6, 16, 8]  | [9, 16, 5]
evaluate_version_2 | [11, 5, 14] | [12, 17, 1] | [9, 21, 0]  | [18, 4, 8]  | [18, 8, 4]
evaluate_version_3 | [8, 6, 16]  | [13, 15, 2] | [15, 15, 0] | [17, 13, 0] | [10, 20, 0]

Gracz niebieski:

evaluation \ depth | 1            | 2           | 3           | 4           | 5
-------------------|--------------|-------------|-------------|-------------|------------
evaluate_random    | [1, 6, 23]   | [2, 4, 24]  | [1, 8, 21]  | [5, 1, 24]  | [3, 10, 17]
evaluate_default   | [9, 11, 10]  | [10, 14, 6] | [8, 19, 3]  | [13, 12, 5] | [14, 12, 4]
evaluate_basic     | [10, 10, 10] | [11, 13, 6] | [8, 19, 3]  | [15, 11, 4] | [13, 13, 4]
evaluate_version_1 | [2, 5, 23]   | [2, 6, 22]  | [3, 15, 12] | [0, 13, 17] | [0, 11, 19]
evaluate_version_2 | [10, 8, 12]  | [7, 12, 11] | [12, 10, 8] | [13, 13, 4] | [12, 16, 2]
evaluate_version_3 | [9, 8, 13]   | [10, 7, 13] | [9, 3, 18]  | [7, 13, 10] | [7, 12, 11]


### Gra na planszy 6x6 z 2 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|------------
evaluate_random    | [2, 1, 27]  | [2, 3, 25]  | [2, 2, 26]  | [8, 0, 22]  | [7, 5, 18]
evaluate_default   | [11, 3, 16] | [11, 17, 2] | [18, 7, 5]  | [23, 6, 1]  | [17, 12, 1]
evaluate_basic     | [10, 4, 16] | [11, 17, 2] | [18, 7, 5]  | [23, 6, 1]  | [15, 15, 0]
evaluate_version_1 | [9, 4, 17]  | [3, 14, 13] | [10, 8, 12] | [12, 10, 8] | [7, 12, 11]
evaluate_version_2 | [6, 8, 16]  | [11, 16, 3] | [17, 8, 5]  | [18, 8, 4]  | [9, 12, 9]
evaluate_version_3 | [10, 3, 17] | [11, 17, 2] | [16, 13, 1] | [16, 13, 1] | [13, 17, 0]

Gracz niebieski:

evaluation \ depth | 1          | 2           | 3           | 4           | 5
-------------------|------------|-------------|-------------|-------------|------------
evaluate_random    | [2, 0, 28] | [4, 0, 26]  | [2, 1, 27]  | [8, 0, 22]  | [6, 2, 22]
evaluate_default   | [5, 6, 19] | [8, 13, 9]  | [12, 11, 7] | [19, 10, 1] | [17, 13, 0]
evaluate_basic     | [6, 4, 20] | [8, 13, 9]  | [12, 10, 8] | [16, 13, 1] | [16, 13, 1]
evaluate_version_1 | [3, 6, 21] | [4, 9, 17]  | [8, 11, 11] | [8, 14, 8]  | [7, 20, 3]
evaluate_version_2 | [6, 7, 17] | [11, 12, 7] | [14, 8, 8]  | [19, 8, 3]  | [16, 10, 4]
evaluate_version_3 | [4, 5, 21] | [10, 11, 9] | [11, 12, 7] | [11, 13, 6] | [13, 13, 4]

### Gra na planszy 5x5 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_random    | [2, 0, 28] | [4, 0, 26] | [2, 1, 27] | [5, 3, 22] | [2, 4, 24]
evaluate_default   | [5, 1, 24] | [5, 5, 20] | [5, 5, 20] | [4, 26, 0] | [4, 26, 0]
evaluate_basic     | [6, 1, 23] | [5, 5, 20] | [5, 5, 20] | [5, 5, 20] | [5, 5, 20]
evaluate_version_1 | [4, 1, 25] | [6, 23, 1] | [7, 23, 0] | [4, 26, 0] | [3, 26, 1]
evaluate_version_2 | [6, 1, 23] | [5, 5, 20] | [4, 5, 21] | [4, 26, 0] | [4, 26, 0]
evaluate_version_3 | [5, 2, 23] | [5, 5, 20] | [5, 5, 20] | [3, 5, 22] | [4, 26, 0]

Gracz niebieski:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|-----------
evaluate_random    | [5, 0, 25]  | [2, 1, 27]  | [4, 4, 22]  | [7, 3, 20]  | [8, 1, 21]
evaluate_default   | [20, 10, 0] | [20, 10, 0] | [20, 10, 0] | [20, 10, 0] | [21, 9, 0]
evaluate_basic     | [9, 21, 0]  | [20, 10, 0] | [5, 25, 0]  | [21, 9, 0]  | [21, 9, 0]
evaluate_version_1 | [13, 8, 9]  | [3, 18, 9]  | [21, 9, 0]  | [10, 20, 0] | [21, 9, 0]
evaluate_version_2 | [20, 10, 0] | [21, 9, 0]  | [21, 9, 0]  | [21, 9, 0]  | [21, 9, 0]
evaluate_version_3 | [21, 9, 0]  | [21, 9, 0]  | [11, 19, 0] | [21, 9, 0]  | [21, 9, 0]


### Gra na planszy 4x4 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|------------
evaluate_random    | [2, 6, 22]  | [5, 2, 23]  | [1, 0, 29]  | [3, 3, 24]  | [4, 4, 22]
evaluate_default   | [15, 1, 14] | [13, 2, 15] | [13, 1, 16] | [15, 15, 0] | [6, 24, 0]
evaluate_basic     | [13, 2, 15] | [13, 3, 14] | [13, 1, 16] | [14, 16, 0] | [5, 25, 0]
evaluate_version_1 | [1, 0, 29]  | [2, 0, 28]  | [14, 0, 16] | [14, 16, 0] | [16, 14, 0]
evaluate_version_2 | [1, 0, 29]  | [15, 0, 15] | [4, 10, 16] | [5, 25, 0]  | [5, 25, 0]
evaluate_version_3 | [15, 1, 14] | [14, 1, 15] | [6, 10, 14] | [6, 24, 0]  | [5, 25, 0]

Gracz niebieski:

evaluation \ depth | 1          | 2           | 3           | 4           | 5
-------------------|------------|-------------|-------------|-------------|------------
evaluate_random    | [4, 0, 26] | [6, 5, 19]  | [5, 3, 22]  | [8, 1, 21]  | [12, 1, 17]
evaluate_default   | [7, 9, 14] | [6, 10, 14] | [19, 11, 0] | [20, 10, 0] | [20, 10, 0]
evaluate_basic     | [8, 8, 14] | [7, 9, 14]  | [19, 11, 0] | [19, 11, 0] | [20, 10, 0]
evaluate_version_1 | [7, 9, 14] | [7, 10, 13] | [7, 12, 11] | [20, 10, 0] | [20, 9, 1]
evaluate_version_2 | [7, 8, 15] | [7, 9, 14]  | [20, 10, 0] | [20, 10, 0] | [20, 10, 0]
evaluate_version_3 | [7, 8, 15] | [6, 10, 14] | [18, 12, 0] | [20, 10, 0] | [20, 10, 0]
