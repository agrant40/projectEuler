#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#Answer is 6857

number = 600851475143

def pf(num):
    factors = []
    d = 2
    while(num > 1):
        while(num % d == 0):
            factors.append(d)
            num = num/d
        d+=1
    return factors

print(max(pf(number)))


