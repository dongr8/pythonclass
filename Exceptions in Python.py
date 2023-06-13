
#Exceptions in Python
#ZeroDivisionError
print('ZeroDivisionError')

a = 10
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("Controlled the flow of zero division error")

print(':::::::::::::::')


#ValueError
print('ValueError')

age = input("Enter your age: ")

try:
    age = int(age)
    if age < 0 or age > 120:
        raise ValueError('Invalid age value')
except ValueError as e:
        print('e')

print(':::::::::::::::')

#TypeError
print('TypeError')

a = 'Hello'

try:
    b= a + 1

except TypeError:
    print("Error: Unsupported Operand Type for +: 'str' and 'int'")

print('::::::::::::::::')

#NameError
print('NameError')

try:
    print(x)
except NameError:
    print('Error: variable X not defined')


#FileNotFoundError
print('::::::::::::::::::')

try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print('Error: File not found')

print(':::::::::::::::::::')

#IndexError
print('IndexError')

a = [1, 2, 3]

try:
    print(a[3])
except IndexError:
    print('Error: List index out of range')

print('::::::::::::::::::::')


#KeyError
print('KeyError')

d = {'a': 1, 'b': 2}
try:
    print(d['c'])
except KeyError:
    print('Error: Key not found')

print('::::::::::::::::::::::::')

#ImportError
print('ImportError')

try:
    import Balablue
    import Bulabah
    import Tinubu
except ImportError:
    print('Error: module not found')


print('::::::::::::::::::::')

#MemoryError
print('MemoryError')

try:
    a = [0] * (10**9)
except MemoryError:
    print('Error: memory error')




























    































