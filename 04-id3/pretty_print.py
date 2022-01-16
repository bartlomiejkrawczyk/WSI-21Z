import pprint
from id3 import Node, Leaf, run_id3
from typing import Union
from reader import read_file


def convert_to_dict(node: Union[Node, Leaf]):
    result = node._asdict()
    if isinstance(node, Node):
        children = {key: convert_to_dict(child)
                    for key, child in node.children.items()}
        result['children'] = children
    return result


def pretty_print(file: str, class_column: int):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(convert_to_dict(
        run_id3(read_file(file, class_column))))
    print()


def main():
    FILES = [('04-id3/data/agaricus-lepiota.data', 0),
             ('04-id3/data/breast-cancer.data', 0),
             ('04-id3/data/car.data', 6),
             ('07-bayesian-network/data/ache.data', 3)]
    for file, class_column in FILES:
        pretty_print(file, class_column)


if __name__ == '__main__':
    main()
