#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Answer is 25164150
import math

def findSumOfSquares(squares):
	list = []
	for square in squares:
		list.append(math.pow(square,2))

	return (sum(list))

def findSquareOfSum(squares):
	return (math.pow(sum(squares),2))

number = 100
squares = []
count = 1

while len(squares) < number:
	squares.append(count)
	count += 1

print (findSquareOfSum(squares) - findSumOfSquares(squares))


