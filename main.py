import math


def main():
    inputs = list(map(float, (input("enter input-")).split()))
    weights = list(map(float, (input("enter weights-")).split()))
    bias = float(input("enter bias-"))
    weighted_sum = bias
    if len(weights) == len(inputs):
        for i in range(len(weights)):
            s = inputs[i] * weights[i]
            weighted_sum += s
    else:
        raise ValueError("no. of weights and inputs are not equal")
    output = 1 / (1 + math.exp(-(weighted_sum)))
    print(output)


main()
