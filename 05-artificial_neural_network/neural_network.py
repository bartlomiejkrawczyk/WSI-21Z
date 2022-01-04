import numpy as np
from numpy import typing as npt
from plotter import plot_functions
from typing import List, Tuple


INDEXES = [310774, 310608]
INDEX_UNITS = [idx % 10 for idx in INDEXES]
PARAMETERS: Tuple[float, float] = (
    (INDEX_UNITS[0] + 1) ** 0.5, (INDEX_UNITS[1] + 1) ** 0.5
)

L_BOUND = -5
U_BOUND = 5


def function_to_approximate(x: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    return (np.sin(x * PARAMETERS[0])  # type: ignore
            + np.cos(x * PARAMETERS[1])
            )


EVAL_X: npt.NDArray[np.float64] = np.linspace(  # type: ignore
    L_BOUND,
    U_BOUND,
    100
)
EVAL_Y = function_to_approximate(EVAL_X)

np.random.seed(1)


def sigmoid(x: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)


def loss(approximated_y: npt.NDArray[np.float64],
         expected_y: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:

    return np.square(approximated_y - expected_y)


def loss_derivative(approximated_y: npt.NDArray[np.float64],
                    expected_y: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:

    return 2 * (approximated_y - expected_y)


def unison_shuffled_copies(a: npt.NDArray[np.float64], b: npt.NDArray[np.float64]) \
        -> Tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    assert len(a) == len(b)
    p: npt.NDArray[np.intc] = np.random.permutation(len(a))  # type: ignore
    return a[p], b[p]


class Network:
    def __init__(self, hidden_layer_sizes: List[int] = []):
        if len(hidden_layer_sizes) == 0:
            hidden_layer_sizes = [13]

        self.sizes = [1]
        self.sizes.extend(hidden_layer_sizes)
        self.sizes.append(1)

        self.weights: List[npt.NDArray[np.float64]] = [
            np.random.uniform(-1.0, 1.0,  # type: ignore
                              size=(self.sizes[i+1], self.sizes[i]))
            for i in range(len(self.sizes) - 2)
        ]
        self.weights.append(
            np.zeros(shape=(self.sizes[-1], self.sizes[-2]))  # type: ignore
        )

        self.biases: List[npt.NDArray[np.float64]] = [
            np.random.uniform(-1.0, 1.0, size=(self.sizes[i+1], 1))
            for i in range(len(self.sizes) - 2)
        ]
        self.biases.append(np.zeros(shape=(self.sizes[-1], 1)))  # type: ignore

    @staticmethod
    def forward(x: npt.NDArray[np.float64],
                weights: npt.NDArray[np.float64],
                biases: npt.NDArray[np.float64],
                activation: bool = True) -> npt.NDArray[np.float64]:

        result = (weights @ x) + biases

        if activation:
            return sigmoid(result)
        return result

    def predict(self, x: float) -> float:
        activations: npt.NDArray[np.float64] = np.array([[x]])  # type: ignore
        for i, values in enumerate(zip(self.weights, self.biases), start=1):
            weights, biases = values
            activations = self.forward(
                activations,
                weights,
                biases,
                i != len(self.weights)
            )

        return activations[0][0]

    def mean_loss(self) -> float:

        return loss(
            np.array([self.predict(x) for x in EVAL_X]),  # type: ignore
            EVAL_Y).mean()  # type: ignore

    def train(self,
              x_set: npt.NDArray[np.float64],
              y_set: npt.NDArray[np.float64],
              iterations: int,
              mini_batch_size: int,
              learning_rate: float) -> None:

        mean_loss_before = self.mean_loss()
        for i in range(iterations):

            self.batch(x_set, y_set, mini_batch_size, learning_rate)

            if i % 100 == 0:
                mean_loss_after = self.mean_loss()
                print(
                    f"Iteration: {i}\tDelta: {mean_loss_after - mean_loss_before}\tMean Loss: {mean_loss_after}"
                )
                mean_loss_before = mean_loss_after

    def batch(self,
              x_set: npt.NDArray[np.float64],
              y_set: npt.NDArray[np.float64],
              mini_batch_size: int,
              learning_rate: float) -> None:

        x_set, y_set = unison_shuffled_copies(x_set, y_set)

        mini_batches = len(x_set) // mini_batch_size

        for i in range(mini_batches):
            start = mini_batch_size * i
            end = start + mini_batch_size

            self.mini_batch(x_set[start:end], y_set[start:end], learning_rate)

    def mini_batch(self,
                   x_set: npt.NDArray[np.float64],
                   y_set: npt.NDArray[np.float64],
                   learning_rate: float) -> None:

        gradient_weights: List[npt.NDArray[np.float64]] = [
            np.zeros(shape=weight.shape)  # type: ignore
            for weight in self.weights
        ]
        gradient_biases: List[npt.NDArray[np.float64]] = [
            np.zeros(shape=bias.shape)  # type: ignore
            for bias in self.biases
        ]
        for x, y in zip(x_set, y_set):
            delta_weights, delta_biases = self.backward(x, y)

            for i, result in enumerate(zip(delta_weights, delta_biases)):
                gradient_weights[i] += result[0]
                gradient_biases[i] += result[1]

        proportion = learning_rate / len(x_set)

        gradient_weights = [
            grad * proportion
            for grad in gradient_weights
        ]
        gradient_biases = [
            grad * proportion
            for grad in gradient_biases
        ]

        self.weights = [
            weight - grad
            for weight, grad in zip(self.weights, gradient_weights)
        ]
        self.biases = [
            bias - grad
            for bias, grad in zip(self.biases, gradient_biases)
        ]

    def backward(self, x: float, expected_y: float) \
            -> Tuple[List[npt.NDArray[np.float64]], List[npt.NDArray[np.float64]]]:

        delta_biases: List[npt.NDArray[np.float64]] = [
            np.zeros(shape=bias.shape)  # type: ignore
            for bias in self.biases
        ]
        delta_weights: List[npt.NDArray[np.float64]] = [
            np.zeros(shape=weight.shape)  # type: ignore
            for weight in self.weights
        ]

        y: npt.NDArray[np.float64] = np.array([[expected_y]])  # type: ignore

        activation: npt.NDArray[np.float64] = np.array([[x]])  # type: ignore
        activations: List[npt.NDArray[np.float64]] = [activation]
        vectors: List[npt.NDArray[np.float64]] = []
        for bias, weight in zip(self.biases, self.weights):
            vector = (weight @ activation) + bias
            vectors.append(vector)
            activation = sigmoid(vector)
            activations.append(activation)

        delta = loss_derivative(vectors[-1], y)
        delta_biases[-1] = delta
        delta_weights[-1] = delta @ activations[-2].T

        for i in range(2, len(self.sizes)):
            vector = vectors[-i]
            d_sigmoid = sigmoid_derivative(vector)
            delta = self.weights[-i+1].T @ delta * d_sigmoid
            delta_biases[-i] = delta
            delta_weights[-i] = delta @ activations[-i-1].T

        return delta_weights, delta_biases


def main():
    training_x: npt.NDArray[np.float64] = np.linspace(  # type: ignore
        L_BOUND,
        U_BOUND,
        10_000
    )

    training_y = function_to_approximate(training_x)

    nn = Network()
    nn.train(training_x, training_y, 1_000, 200, 1e-1)

    approximated_y: npt.NDArray[np.float64] = np.array(  # type: ignore
        [nn.predict(x) for x in training_x]
    )

    plot_functions(training_x, training_y, approximated_y)


if __name__ == '__main__':
    main()
