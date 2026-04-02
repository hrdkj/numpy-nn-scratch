import math

import numpy as np


def main():
    inputs = np.array(list(map(float, input("enter inputs-").split())))
    weights = np.array(list(map(float, input("enter weights-").split()))).reshape(4,3)
    bias = float(input("enter bias-"))
    if weights.shape[1] == len(inputs):
        s = np.dot(weights, inputs)
        weighted_sum = s + bias
    else:
        raise ValueError("no. of weights and inputs are not equal")
    output = 1 / (1 + np.exp(-(weighted_sum)))
    print(output)


main()
