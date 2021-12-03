from typing import List, NamedTuple, Union, Dict
from collections import Counter
from functools import partial
from math import log


class TrainingData(NamedTuple):
    class_: str
    values: List[str]


class Leaf(NamedTuple):
    predicted_class: str

    def get_class(self, sample: List[str]) -> str:
        return self.predicted_class


class Node(NamedTuple):
    attribute: int
    children: Dict[str, Union['Node', Leaf]]

    def get_class(self, sample: List[str]) -> str:
        if sample[self.attribute] in self.children:
            return self.children[sample[self.attribute]].get_class(sample)

        classes: List[str] = [
            child.get_class(sample)
            for child in self.children.values()
        ]

        class_counter = Counter(classes)

        return class_counter.most_common(1)[0][0]


def split_data(attribute: int, data: List[TrainingData]) -> Dict[str, List[TrainingData]]:
    dictionary: Dict[str, List[TrainingData]] = {}
    for sample in data:
        dictionary.setdefault(sample.values[attribute], []).append(sample)
    return dictionary


def entropy(class_counter: "Counter[str]") -> float:
    return - sum(count * log(count) for count in class_counter.values())


def inf(attribute: int, data: List[TrainingData]) -> float:
    splitted_data = split_data(attribute, data)
    return sum(
        entropy(Counter(sample.class_ for sample in subset)) *
        len(subset) / len(data)
        for subset in splitted_data.values()
    )


def inf_gain(attribute: int, data: List[TrainingData], class_counter: "Counter[str]") -> float:
    return entropy(class_counter) - inf(attribute, data)


def id3(data: List[TrainingData], attributes: List[int]) -> Union[Node, Leaf]:
    class_counter = Counter(sample.class_ for sample in data)

    if len(class_counter) == 1:
        return Leaf(data[0].class_)

    if len(attributes) == 0:
        return Leaf(class_counter.most_common(1)[0][0])

    attribute = max(
        attributes,
        key=partial(
            inf_gain,
            data=data,
            class_counter=class_counter
        )  # type: ignore
    )
    attributes.remove(attribute)

    splitted_data = split_data(attribute, data)

    return Node(attribute, {new_attribute: id3(new_data, attributes) for new_attribute, new_data in splitted_data.items()})


def run_id3(data: List[TrainingData]) -> Union[Node, Leaf]:
    return id3(data, list(range(len(data[0].values))))


def main():
    tree = run_id3([
        TrainingData('A', ['1', '2', '3']),
        TrainingData('A', ['2', '2', '3']),
        TrainingData('B', ['1', '1', '3']),
        TrainingData('C', ['3', '1', '2'])
    ])

    print(tree)
    print(tree.get_class(['3', '1', '2']))
    print(tree.get_class(['6', '2', '7']))


if __name__ == '__main__':
    main()
