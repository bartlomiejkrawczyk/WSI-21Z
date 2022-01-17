from typing import List, NamedTuple, Dict
from random import uniform
import json
from collections import OrderedDict

DATA_FILE = '07-bayesian-network/data/ache.json'
FILE_TO_GENERATE = '07-bayesian-network/data/ache.data'

NUMBER_OF_SAMPLES = 10_000


class Variable(NamedTuple):
    name: str
    depends_on: List[str]
    probabilities: Dict[str, float]


class Sample:
    def __init__(self, variables: List[Variable]) -> None:
        self.values: OrderedDict[str, str] = OrderedDict()
        for variable in variables:
            parent_values = ''
            for name in variable.depends_on:
                parent_values += self.values[name]

            self.values[variable.name] = (
                'T'
                if uniform(0, 1) < variable.probabilities[parent_values]
                else 'F'
            )

    def __str__(self) -> str:
        result = ''
        for val in self.values.values():
            result += val + ','
        return result[:-1]


def load_variables_from_json(filepath: str = DATA_FILE) -> List[Variable]:
    with open(filepath, 'r') as handle:
        data = json.load(handle)

    variables: List[Variable] = []

    for variable in data:
        name = variable['name']
        depends_on = variable['depends_on']
        probabilities = variable['probabilities']

        variables.append(Variable(name, depends_on, probabilities))

    return variables


def generate_data(variables: List[Variable], filepath: str = FILE_TO_GENERATE) -> None:
    with open(filepath, 'w') as handle:
        for _ in range(NUMBER_OF_SAMPLES):
            handle.write(str(Sample(variables)) + '\n')


def print_statistics(variables: List[Variable], filepath: str = FILE_TO_GENERATE):

    with open(filepath, 'r') as handle:
        lines = handle.readlines()

    print('name|frequency', '-|-', sep='\n')
    for idx, variable in enumerate(variables):
        counts = {'T': 0, 'F': 0}
        for line in lines:
            counts[str(line[idx * 2])] += 1
        print(variable.name, counts['T'] / NUMBER_OF_SAMPLES, sep='|')


def main():
    variables = load_variables_from_json()
    generate_data(variables)
    print_statistics(variables)


if __name__ == '__main__':
    main()
