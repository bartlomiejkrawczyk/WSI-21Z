

### Gra na planszy 8x8 z 3 rzędami pionów na starcie vs przeciwnik z ustawioną funkcją ewaluującą podstawową i głębokością 3.

Gracz biały:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_default   | draw | draw | draw | win  | draw
evaluate_basic     | draw | draw | draw | win  | draw
evaluate_version_1 | lose | draw | lose | draw | draw
evaluate_version_2 | lose | draw | draw | lose | draw
evaluate_version_3 | draw | draw | draw | win  | draw

Gracz niebieski:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_default   | lose | lose | draw | win  | lose
evaluate_basic     | lose | lose | draw | win  | lose
evaluate_version_1 | lose | lose | lose | lose | lose
evaluate_version_2 | lose | lose | draw | draw | draw
evaluate_version_3 | lose | lose | lose | lose | draw

### Gra na planszy 8x8 z 3 rzędami pionów na starcie, każdy z każdym.


### Gra na planszy 6x6 z 2 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2           | 3           | 4           | 5
-------------------|------------|-------------|-------------|-------------|------------
evaluate_default   | [6, 3, 16] | [6, 17, 2]  | [13, 7, 5]  | [18, 6, 1]  | [13, 12, 0]
evaluate_basic     | [6, 3, 16] | [6, 17, 2]  | [13, 7, 5]  | [18, 6, 1]  | [10, 15, 0]
evaluate_version_1 | [7, 3, 15] | [1, 13, 11] | [6, 8, 11]  | [8, 10, 7]  | [3, 12, 10]
evaluate_version_2 | [2, 8, 15] | [6, 16, 3]  | [12, 8, 5]  | [13, 8, 4]  | [4, 12, 9]
evaluate_version_3 | [6, 3, 16] | [6, 17, 2]  | [11, 13, 1] | [11, 13, 1] | [8, 17, 0]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3           | 4           | 5
-------------------|------------|------------|-------------|-------------|------------
evaluate_default   | [3, 3, 19] | [3, 13, 9] | [8, 10, 7]  | [14, 10, 1] | [12, 13, 0]
evaluate_basic     | [3, 3, 19] | [3, 13, 9] | [8, 10, 7]  | [11, 13, 1] | [12, 13, 0]
evaluate_version_1 | [0, 4, 21] | [0, 8, 17] | [3, 11, 11] | [3, 14, 8]  | [3, 20, 2]
evaluate_version_2 | [3, 6, 16] | [6, 12, 7] | [9, 8, 8]   | [14, 8, 3]  | [11, 10, 4]
evaluate_version_3 | [2, 4, 19] | [5, 11, 9] | [7, 12, 6]  | [7, 12, 6]  | [8, 13, 4]

### Gra na planszy 5x5 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_default   | [2, 1, 22] | [0, 5, 20] | [0, 5, 20] | [0, 25, 0] | [0, 25, 0]
evaluate_basic     | [2, 1, 22] | [0, 5, 20] | [0, 5, 20] | [0, 5, 20] | [0, 5, 20]
evaluate_version_1 | [2, 1, 22] | [2, 23, 0] | [2, 23, 0] | [0, 25, 0] | [0, 25, 0]
evaluate_version_2 | [2, 1, 22] | [0, 5, 20] | [0, 5, 20] | [0, 25, 0] | [0, 25, 0]
evaluate_version_3 | [2, 1, 22] | [0, 5, 20] | [0, 5, 20] | [0, 4, 21] | [0, 25, 0]

Grach niebieski:

evaluation \ depth | 1          | 2           | 3          | 4          | 5
-------------------|------------|-------------|------------|------------|-----------
evaluate_default   | [16, 9, 0] | [16, 9, 0]  | [16, 9, 0] | [16, 9, 0] | [16, 9, 0]
evaluate_basic     | [5, 20, 0] | [15, 10, 0] | [0, 25, 0] | [16, 9, 0] | [16, 9, 0]
evaluate_version_1 | [11, 7, 7] | [1, 17, 7]  | [16, 9, 0] | [5, 20, 0] | [16, 9, 0]
evaluate_version_2 | [16, 9, 0] | [16, 9, 0]  | [16, 9, 0] | [16, 9, 0] | [16, 9, 0]
evaluate_version_3 | [16, 9, 0] | [16, 9, 0]  | [6, 19, 0] | [16, 9, 0] | [16, 9, 0]


### Gra na planszy 4x4 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1           | 2           | 3           | 4           | 5
-------------------|-------------|-------------|-------------|-------------|------------
evaluate_default   | [10, 1, 14] | [10, 1, 14] | [11, 0, 14] | [11, 14, 0] | [1, 24, 0]
evaluate_basic     | [10, 1, 14] | [10, 1, 14] | [11, 0, 14] | [11, 14, 0] | [0, 25, 0]
evaluate_version_1 | [0, 0, 25]  | [0, 0, 25]  | [11, 0, 14] | [9, 16, 0]  | [11, 14, 0]
evaluate_version_2 | [0, 0, 25]  | [11, 0, 14] | [1, 10, 14] | [1, 24, 0]  | [0, 25, 0]
evaluate_version_3 | [10, 1, 14] | [10, 1, 14] | [1, 10, 14] | [1, 24, 0]  | [0, 25, 0]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3           | 4           | 5
-------------------|------------|------------|-------------|-------------|------------
evaluate_default   | [3, 8, 14] | [3, 8, 14] | [15, 10, 0] | [15, 10, 0] | [15, 10, 0]
evaluate_basic     | [3, 8, 14] | [3, 8, 14] | [15, 10, 0] | [15, 10, 0] | [15, 10, 0]
evaluate_version_1 | [3, 8, 14] | [3, 9, 13] | [3, 11, 11] | [15, 10, 0] | [15, 9, 1]
evaluate_version_2 | [3, 8, 14] | [3, 8, 14] | [15, 10, 0] | [15, 10, 0] | [15, 10, 0]
evaluate_version_3 | [3, 8, 14] | [3, 8, 14] | [15, 10, 0] | [15, 10, 0] | [15, 10, 0]
