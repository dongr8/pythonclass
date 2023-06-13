def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

a = factorial(10)
print(a)


def cursive(n):
    if n == 0:
        return 1
    else:
        return n * cursive(n - 1)
b = cursive(5)
print(b)


def john(m):
    if m == 0:
        return 1
    else:
        return m * john(m - 1)
c = john(15)
print(c)


#Fabonacci
#fn = fn -1 + fn
#F must be > 1 for it to run

def fibonacci(john):
    if john == 0:
        return 0   #f0 = 0
    elif john ==1: #f1 = 1
        return 1   #john > 1
    else:
        return fibonacci(john-1) + fibonacci(john-2)
f = fibonacci(8)
print(f)
