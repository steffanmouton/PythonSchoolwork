# FizzBuzz, 3, 5

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"

for i in range(0,16):
    print i, fizzbuzz(i)