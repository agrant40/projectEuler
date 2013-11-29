__author__ = 'Adam'


#Answer 4613732
numberList = [1,2]
number = 0
count = 1

while (numberList[-1] < 4000000):
	number = numberList[count - 1] + numberList[count]
	numberList.append(number)
	count += 1

print (numberList)

evenList = []

for num in numberList:
	if num % 2 == 0:
		evenList.append(num)
print ('--------------------------')
print (evenList)
print ('--------------------------')
print (sum(evenList))