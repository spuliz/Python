# A palindromic number reads the same both ways. The largest palindromic number
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindromic number made from the product of two 3-digit numbers.
# Use functions to break down your code!

limit = 999*999

def MaxPalindromic(p):
    palindromic = []
    for n in range(0, p+1):
        n = str(n)
        a = int(n[0:])
        b = int(n[::-1])
        if a == b:
            palindromic.append(n)
    return palindromic[-1]

print(MaxPalindromic(limit))
