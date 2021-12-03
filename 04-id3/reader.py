from id3 import TrainingData
from typing import List
import csv


def read_file(file: str, class_column: int = 0) -> List[TrainingData]:
    data: List[TrainingData] = []
    with open(file, 'r') as handle:
        reader = csv.reader(handle)

        for values in reader:
            class_ = values[class_column]
            val: List[str] = []
            if class_column != 0:
                val.extend(values[: class_column])
            if class_column != len(values) - 1:
                val.extend(values[class_column + 1:])
            data.append(TrainingData(class_, val))
    return data


def main():
    for val in read_file('04-id3/data/agaricus-lepiota.data', 0):
        print(val)


if __name__ == '__main__':
    main()
