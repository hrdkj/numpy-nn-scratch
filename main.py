import math

import numpy as np


def main():
    inputs = np.array(list(map(float, input("enter inputs-").split())))
    weights = np.array(list(map(float, input("enter weights-").split())))
    bias = float(input("enter bias-"))
    if len(weights) == len(inputs):
        s = np.dot(inputs,weights)
        weighted_sum = s + bias
    else:
        raise ValueError("no. of weights and inputs are not equal")
    output = 1 / (1 + math.exp(-(weighted_sum)))
    print(output)


main()
