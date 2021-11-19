4 / 1

evaluation \ depth | 1         | 2         | 3         | 4         | 5
-------------------|-----------|-----------|-----------|-----------|----------
evaluate_basic     | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0]
evaluate_version_1 | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0]
evaluate_version_2 | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0]
evaluate_version_3 | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0] | [1, 0, 0]

evaluation \ depth | 1         | 2         | 3         | 4         | 5
-------------------|-----------|-----------|-----------|-----------|----------
evaluate_basic     | [0, 0, 1] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1]
evaluate_version_1 | [1, 0, 0] | [1, 0, 0] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1]
evaluate_version_2 | [1, 0, 0] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1]
evaluate_version_3 | [0, 0, 1] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1] | [0, 0, 1]

8 / 3

evaluation \ depth | 1    | 2    | 3   | 4   | 5
-------------------|------|------|-----|-----|-----
evaluate_basic     | draw | win  | win | win | win
evaluate_version_1 | win  | win  | win | win | win
evaluate_version_2 | win  | draw | win | win | draw
evaluate_version_3 | win  | win  | win | win | win

evaluation \ depth | 1    | 2    | 3    | 4    | 5
-------------------|------|------|------|------|-----
evaluate_basic     | lose | lose | lose | lose | lose
evaluate_version_1 | draw | draw | draw | draw | draw
evaluate_version_2 | lose | lose | lose | lose | lose
evaluate_version_3 | lose | lose | lose | draw | draw


8 / 3 - full

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [2, 6, 8]  | [12, 6, 2] | [13, 7, 0] | [13, 6, 1] | [12, 5, 2]
evaluate_version_1 | [18, 2, 0] | [16, 4, 0] | [15, 5, 0] | [13, 4, 3] | [15, 5, 0]
evaluate_version_2 | [8, 3, 9]  | [11, 7, 2] | [10, 9, 1] | [11, 7, 2] | [13, 5, 2]
evaluate_version_3 | [5, 5, 9]  | [13, 6, 1] | [13, 6, 1] | [14, 6, 0] | [12, 6, 1]

evaluation \ depth | 1          | 2          | 3          | 4          | 5
-------------------|------------|------------|------------|------------|-----------
evaluate_basic     | [4, 4, 11] | [0, 7, 12] | [1, 7, 11] | [4, 8, 7]  | [4, 4, 11]
evaluate_version_1 | [0, 3, 17] | [0, 4, 16] | [0, 6, 14] | [1, 2, 17] | [2, 5, 13]
evaluate_version_2 | [4, 7, 9]  | [1, 6, 13] | [3, 8, 9]  | [4, 6, 10] | [4, 4, 12]
evaluate_version_3 | [3, 3, 13] | [1, 4, 15] | [1, 9, 10] | [4, 7, 9]  | [3, 6, 10]