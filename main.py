import math
def main():
    print("Hello from numpy-nn-scratch!")
    a = float(input())
    b = float(input())
    c = float(input())
    age = int(input("enter your age-"))
    weight = float(input("Enter your weight-"))
    sugar = int(input("Enter your blood sugar level-"))
    x1 = age / 100
    x2 = weight / 150
    x3 = (sugar - 70 )/ 330
    weighted_sum = a*x1 + b*x2 + c*x3
    output = 1/ (1+ math.exp(-(weighted_sum)))
    print(output)

main()

