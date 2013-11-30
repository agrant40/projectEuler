#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#Answer is 232792560

def isDivisibleByAll(number):
    remainder = 0
    for x in range(1,20):
        remainder += number%x
    return remainder == 0

startNum = 10000
while(isDivisibleByAll(startNum) == False):
    startNum += 20

print(startNum)