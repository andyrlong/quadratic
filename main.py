# quadratic.py
# A program that computes the real roots of a quadratic equation

import math

def main():
    print("This program finds the real solutions to a quadratic.")
    print()

    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficinet b: "))
    c = float(input("Enter coefficinet c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are:", root1, root2)
    
main()

