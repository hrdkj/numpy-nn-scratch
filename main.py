import math
def main():
    print("Hello from numpy-nn-scratch!")
    w1 = float(input())
    w2 = float(input())
    w3 = float(input())
    age = int(input("enter your age-"))
    weight = float(input("Enter your weight-"))
    sugar = int(input("Enter your blood sugar level-"))
    b = float(input("Enter bias:"))
    x1 = age / 100
    x2 = weight / 150
    x3 = (sugar - 70 )/ 330
    weighted_sum = w1*x1 + w2*x2 + w3*x3 + b
    output = 1/ (1+ math.exp(-(weighted_sum)))
    print(output)

main()

