import random


def add_two():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    num3 = num1 + num2
    res = int(input("what is {} + {}?".format(num1, num2)))
    if res == num3:
        print("True")
    else:
        print("False")

add_two()
