

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sumDigits(n):
    s = str(n)
    def addDigits(s):
        if len(s) == 1:
            return int(s)
        else:
            return addDigits(s[:-1]) + int(s[len(s)-1])
    return addDigits(s)

f = (factorial(100))
print sumDigits(f)
