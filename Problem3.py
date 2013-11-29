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


