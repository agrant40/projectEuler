#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#Answer is 104743
import math

def isPrime(number):
	if number == 2:
		return True
	elif number % 2 == 0:
		return False
	count = 3
	range = int(math.sqrt(number)) + 1
	while count < range:
		if number % count == 0:
			return False
		count += 1
	return True

primeCounter = 1
count = 3
while primeCounter < 10001:
	if isPrime(count):
		primeCounter += 1
	count += 2

print (count - 2)