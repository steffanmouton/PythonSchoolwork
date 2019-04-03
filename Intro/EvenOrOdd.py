# name: is_odd_or_even(number): function to detemrine if a number is even or odd
# input: number->integer value
# output: print the number and "is odd" or "is even"

def is_odd_or_even(number):
    if (number % 2 == 0):
        return number, "is even"
    else:
        return number, "is odd"

for i in range(0, 11):
    print(is_odd_or_even(i))
