#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#Answer is 142913828922
def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    max = num ** 0.5 + 1
    i = 3

    while i <= max:
        if num % i == 0:
            return False
        i += 2

    return True

count = 1
primeList = []
while count < 2000000:
    if isPrime(count):
        primeList.append(count)
    count += 1

print(sum(primeList))


