import numpy as np
from numpy import typing as npt
from plotter import plot_functions


INDEXES = [310774, 310774]
INDEX_UNITS = [idx % 10 for idx in INDEXES]


L_BOUND = -5
U_BOUND = 5


def function_to_approximate(x: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    return np.sin(x * np.sqrt(INDEX_UNITS[0] + 1)) + np.cos(x * np.sqrt(INDEX_UNITS[1] + 1))


X: npt.NDArray[np.float32] = np.linspace(L_BOUND, U_BOUND, 100)  # type: ignore
Y = function_to_approximate(X)

np.random.seed(1)


# f logistyczna jako przykład sigmoidalej
def sigmoid(x: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    return 1 / (1 + np.exp(-x))


# pochodna fun. 'sigmoid'
def d_sigmoid(x: npt.NDArray[np.float32]) -> npt.NDArray[np.float32]:
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)


#f. straty
def nloss(approximated_y: float, y: float) -> float:
    return (approximated_y - y) ** 2


# pochodna f. straty
def d_nloss(approximated_y: float, y: float) -> float:
    return 2 * (approximated_y - y)


class Network:
    def __init__(self, x: npt.NDArray[np.float32], y: npt.NDArray[np.float32], hidden_layer_size: int = 9):
        self.x = x
        self.y = y
        # self.approximated_y = 0

        self.hidden_layer_size = hidden_layer_size
        self.LR = 0.003

        # TODO:

    def forward(self, x: npt.NDArray[np.float32]):
        pass  # TODO:

    def predict(self, x: npt.NDArray[np.float32]):
        # TODO:
        return

    def backward(self, x: npt.NDArray[np.float32], y: npt.NDArray[np.float32]):
        # TODO:
        pass

    def train(self, x_set: npt.NDArray[np.float32], y_set: npt.NDArray[np.float32], iterations: int):
        for _ in range(iterations):
            # TODO:
            pass


def main():
    nn = Network(X, Y)
    nn.train(X, Y, 15000)

    approximated_y = Y / 2  # TODO: tu umiescić wyniki (y) z sieci

    plot_functions(X, Y, approximated_y)


if __name__ == '__main__':
    main()
