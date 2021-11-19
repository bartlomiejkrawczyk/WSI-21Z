

### Gra na planszy 8x8 z 3 rzędami pionów na starcie vs przeciwnik z ustawioną funkcją ewaluującą podstawową i głębokością 3.

Gracz biały:

evaluation \ depth | 1    | 2    | 3   | 4   | 5
-------------------|------|------|-----|-----|-----
evaluate_basic     | draw | win  | win | win | win
evaluate_version_1 | win  | win  | win | win | win
evaluate_version_2 | win  | draw | win | win | draw
evaluate_version_3 | win  | win  | win | win | win

Gracz niebieski:

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_basic     | lose | lose | lose | lose | lose
evaluate_version_1 | draw | draw | draw | draw | draw
evaluate_version_2 | lose | lose | lose | lose | lose
evaluate_version_3 | lose | lose | lose | draw | draw


### Gra na planszy 8x8 z 3 rzędami pionów na starcie, każdy z każdym.

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [2, 9, 9]  | [12, 6, 2] | [13, 7, 0] | [13, 6, 1] | [12, 6, 2]
evaluate_version_1 | [18, 2, 0] | [16, 4, 0] | [15, 5, 0] | [13, 4, 3] | [15, 5, 0]
evaluate_version_2 | [8, 3, 9]  | [11, 7, 2] | [10, 9, 1] | [11, 7, 2] | [13, 5, 2]
evaluate_version_3 | [5, 6, 9]  | [13, 6, 1] | [13, 6, 1] | [14, 6, 0] | [12, 7, 1]

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [3, 1, 16] | [0, 2, 18] | [0, 3, 17] | [4, 2, 14] | [3, 2, 15]
evaluate_version_1 | [4, 11, 5] | [2, 16, 2] | [5, 13, 2] | [3, 12, 5] | [6, 10, 4]
evaluate_version_2 | [2, 3, 15] | [0, 1, 19] | [0, 8, 12] | [4, 7, 9]  | [1, 6, 13]
evaluate_version_3 | [3, 3, 14] | [0, 3, 17] | [0, 7, 13] | [2, 3, 15] | [3, 3, 14]

### Gra na planszy 6x6 z 2 rzędami pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [12, 6, 2] | [16, 3, 1] | [14, 4, 2] | [17, 3, 0] | [14, 3, 3]
evaluate_version_1 | [12, 8, 0] | [5, 13, 2] | [16, 2, 2] | [9, 7, 4]  | [13, 7, 0]
evaluate_version_2 | [9, 9, 2]  | [14, 6, 0] | [13, 6, 1] | [14, 5, 1] | [13, 7, 0]
evaluate_version_3 | [13, 6, 1] | [16, 3, 1] | [17, 3, 0] | [17, 2, 1] | [15, 2, 3]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [0, 2, 18] | [0, 3, 17] | [0, 8, 12] | [0, 2, 18] | [1, 1, 18]
evaluate_version_1 | [13, 4, 3] | [7, 5, 8]  | [3, 7, 10] | [1, 6, 13] | [0, 17, 3]
evaluate_version_2 | [1, 4, 15] | [0, 3, 17] | [0, 9, 11] | [0, 11, 9] | [0, 6, 14]
evaluate_version_3 | [0, 0, 20] | [0, 1, 19] | [0, 5, 15] | [0, 5, 15] | [0, 6, 14]

### Gra na planszy 5x5 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [0, 16, 4] | [13, 0, 7] | [20, 0, 0] | [11, 3, 6] | [11, 3, 6]
evaluate_version_1 | [11, 6, 3] | [14, 6, 0] | [15, 4, 1] | [12, 8, 0] | [11, 3, 6]
evaluate_version_2 | [0, 7, 13] | [19, 0, 1] | [20, 0, 0] | [11, 3, 6] | [11, 3, 6]
evaluate_version_3 | [0, 7, 13] | [13, 0, 7] | [20, 0, 0] | [11, 3, 6] | [11, 3, 6]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [3, 0, 17] | [3, 8, 9]  | [0, 4, 16] | [11, 4, 5] | [11, 4, 5]
evaluate_version_1 | [3, 0, 17] | [0, 3, 17] | [0, 4, 16] | [4, 4, 12] | [0, 3, 17]
evaluate_version_2 | [3, 0, 17] | [3, 9, 8]  | [0, 4, 16] | [11, 4, 5] | [11, 4, 5]
evaluate_version_3 | [3, 0, 17] | [3, 8, 9]  | [0, 4, 16] | [11, 4, 5] | [11, 4, 5]


### Gra na planszy 4x4 z 1 rzędem pionów na starcie, każdy z każdym.

Gracz biały:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [16, 1, 3] | [17, 0, 3] | [17, 0, 3] | [16, 1, 3] | [16, 1, 3]
evaluate_version_1 | [16, 1, 3] | [17, 3, 0] | [11, 9, 0] | [14, 3, 3] | [16, 1, 3]
evaluate_version_2 | [16, 1, 3] | [17, 0, 3] | [17, 0, 3] | [16, 1, 3] | [16, 1, 3]
evaluate_version_3 | [16, 1, 3] | [17, 0, 3] | [17, 0, 3] | [16, 1, 3] | [16, 1, 3]

Gracz niebieski:

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [0, 1, 19] | [0, 2, 18] | [0, 0, 20] | [0, 0, 20] | [0, 0, 20]
evaluate_version_1 | [18, 1, 1] | [18, 1, 1] | [0, 0, 20] | [0, 1, 19] | [0, 12, 8]
evaluate_version_2 | [18, 1, 1] | [0, 2, 18] | [0, 1, 19] | [0, 1, 19] | [0, 0, 20]
evaluate_version_3 | [0, 1, 19] | [0, 2, 18] | [0, 0, 20] | [0, 0, 20] | [0, 0, 20]