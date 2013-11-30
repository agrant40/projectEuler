#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#Answer is 906609

def isPalindrome(num):
    stNum = str(num)
    return(stNum == stNum[::-1])

maxPalindrome = 0
for x in range(100,999):
    for y in range(100,999):
        if isPalindrome(x * y):
            if x * y > maxPalindrome:
                maxPalindrome = x * y


print(maxPalindrome)

