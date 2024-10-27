def fac(n):
    factorial = 1
    for i in range(n):
        factorial = factorial * (i+1)
    return factorial
a = fac(5)
print(a)
print(fac(10))
