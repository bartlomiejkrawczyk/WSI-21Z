from typing import List, NamedTuple, Union, Dict
from collections import Counter
from functools import partial
from math import log


class TrainingData(NamedTuple):
    expected_class: str
    values: List[str]


class Leaf(NamedTuple):
    predicted_class: str

    def identify(self, _sample: List[str]) -> str:
        return self.predicted_class


class Node(NamedTuple):
    attribute: int
    children: Dict[str, Union['Node', Leaf]]

    def identify(self, sample: List[str]) -> str:
        if sample[self.attribute] in self.children:
            return self.children[sample[self.attribute]].identify(sample)

        classes: List[str] = [
            child.identify(sample)
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
    total = sum(class_counter.values())
    return -sum(count / total * log(count / total) for count in class_counter.values())


def inf(attribute: int, data: List[TrainingData]) -> float:
    splitted_data = split_data(attribute, data)
    return sum(
        len(subset) / len(data) *
        entropy(Counter(sample.expected_class for sample in subset))
        for subset in splitted_data.values()
    )


def inf_gain(attribute: int, data: List[TrainingData], class_counter: "Counter[str]") -> float:
    return entropy(class_counter) - inf(attribute, data)


def id3(data: List[TrainingData], attributes: List[int]) -> Union[Node, Leaf]:
    class_counter = Counter(sample.expected_class for sample in data)

    if len(class_counter) == 1:
        return Leaf(data[0].expected_class)

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
    attributes = attributes.copy()
    attributes.remove(attribute)

    splitted_data = split_data(attribute, data)

    return Node(attribute, {new_attribute: id3(new_data, attributes) for new_attribute, new_data in splitted_data.items()})


def run_id3(data: List[TrainingData]) -> Union[Node, Leaf]:
    return id3(data, list(range(len(data[0].values))))


def main():

    data = [
        TrainingData('0', ['A', '1']),
        TrainingData('1', ['B', '1']),
        TrainingData('1', ['B', '2']),
        TrainingData('0', ['B', '2']),
        TrainingData('1', ['B', '3'])
    ]

    tree = run_id3(data)
    print(tree)
    print()

    print(inf_gain(0, data, Counter(sample.expected_class for sample in data)))
    print()

    print(tree.identify(['A', '1']))
    print(tree.identify(['B', '1']))
    print(tree.identify(['B', '2']))
    print(tree.identify(['B', '3']))


if __name__ == '__main__':
    main()
