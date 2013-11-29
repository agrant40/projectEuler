__author__ = 'Adam'

#Answer is 233168
number = 0
numberList = []

for number in range(1, 1000):
	if number % 3 == 0:
		numberList.append(number)
	elif number % 5 == 0:
		numberList.append(number)

print (sum(numberList))