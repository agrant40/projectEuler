#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#Answer is (200, 375, 425, 31875000)

def findABCandProduct(sum):
    for i in range(1, sum, 1):
        for j in range(1, sum - i, 1):
            k = sum - i - j
            if i ** 2 + j ** 2 == k ** 2:
                return i, j, k, i * j * k

print(findABCandProduct(1000))