import math

import numpy as np


def main():
    inputs = np.array(list(map(float, input("enter inputs-").split())))
    weights = np.array(list(map(float, input("enter weights-").split()))).reshape(4,3)
    bias = float(input("enter bias-"))
    assert weights.shape[1] == len(inputs), "shape mismatch"
    s = np.dot(weights, inputs)
    weighted_sum = s + bias
    output = 1 / (1 + np.exp(-(weighted_sum)))
    print(output)


main()
