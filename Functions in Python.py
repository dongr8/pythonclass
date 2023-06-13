

#User difined Function

def add(a, b):
    return a + b
result = add(2, 4)
print(result)

print(':::::::::::::::::')

def multiply(a, b):
    return a * b
output = multiply(2,3)
print(output)

print(':::::::::::::::::')
#Exampples of Built-in Function

#print
#len For numbers/Integars
#range For String/alpabets

for x in range(10):
    print(x)

print(':::::::::::::::::')

a = ('Hello World!')
print(len(a))

print(':::::::::::::::::')

name = input("whats your name? ")
print("My name is "+ name + "!")#Add your space in the str without sringing for space.

print(':::::::::::::::::')

my_max = [1, 2, 5, 3, 7]
print(max(my_max))

print(':::::::::::::::::')

my_min = [1, 2, 5, 3, 7]
print(min(my_min))

print(':::::::::::::::::')

my_sum = [1, 2, 5, 3, 7]
print(sum(my_max))

print(':::::::::::::::::')

#Lambda function

square = lambda x: x ** 3
result = square(5)
print(result)

print(':::::::::::::::::')

square = lambda x: x ** 3 + 10
result = square(5)
print(result)

print(':::::::::::::::::')

my_list = [(1, 3), (2, 1), (3, 2), (2, 4)]
sorted_list = sorted(my_list, key=lambda x: x[1])# "Key"=lambda is a key word
print(sorted_list)

print(':::::::::::::::::')

my_sorted = [1, 2, 5, 3, 7, 9, 8]
print(sorted(my_sorted))

print(':::::::::::::::::')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)

print(':::::::::::::::::')


def area_of_circle(radius):
    area =3.14 * radius **2
    return (area)
#Calling the function
total = area_of_circle(20)
print(total)

print(':::::::::::::::::')

def greeting(name, message= "Hello"):
    return f"{message}, {name}!"
result = greeting("Allice")
print(result)



























