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