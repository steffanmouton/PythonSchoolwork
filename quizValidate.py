#Create a function A that will validate expected output of a tuple B in the form (function, args).
#The expected output C will be given to A to validate testing
import math
def sum(tup):
	new = tup[0] + tup[1]
	return new

def pt(sidesAB):
    	return float(math.sqrt(pow(sidesAB[0], 2) + pow(sidesAB[1], 2)))
	
def validate(test, expected):
	return test[0](test[1]) == expected

alpha = 10
beta = 10
e1 = 20

sideA = 6
sideB = 8
e2 = 10
eWrong = 12

t1 = validate((sum, [alpha,beta]), e1)
# Expect t1 == True
t2 = validate((pt, [sideA, sideB]), e2)
# Expect t2 == True
t3 = validate((pt, [sideA, sideB]), eWrong)
# Expect t3 == False