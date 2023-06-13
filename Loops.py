
fruits = ["apple", "banana", "charry"]
for fruit in fruits:
    print(fruits)

#Note that the For (variable) can be anything,
#what matters is the main variable fruits eg...


print("********************")

fruits = ["apple", "banana", "charry"]
for cheese in fruits:
    print(fruits)

print("********************")

fruits = ["apple", "banana", "charry"]
for cheese in fruits:
    print(cheese)

print("********************")

for x in fruits:
    print(x)

print("********************")

#While Loop

a =0
while a<5:
    print(a)
    a+=1

print("********************")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    result = num**2
    print("The sqaure of", num, "is", result)
    
print("********************")

string = "hello"
for char in string:
    ascii_code = ord(char)
    print("The ASII code of", char, "is", ascii_code)

print("********************")

sum = 0
for i in range(5):
    sum = sum + 1
    print("The current sum is", sum)
    print("The final sum is", sum)

print("********************")

people = [{"name": "Alie", "age": 30}, {'name': 'bob', 'age': 20}]
for person in people:
    name = person['name']
    age = person['age']
    print("The person's name is", name, "and their age is", age)

print("********************")

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sublist in lists:
    first_item = sublist[2]
    print("The first item in the sublist is", first_item)

print("********************")

#Working with enuerate function

fruits = ["apple", "banana", "cherry"]
for x, fruit in enumerate(fruits):
    print("The fruit atindex", x, "is", fruit)

print("********************")

fruits = ["apple", "banana", "cherry"]
for fruit in enumerate(fruits):
    print("The fruit atindex is", fruit)

print("********************")

colors = ["red", "green", "blue"]
names = ["rose", "leaf", "sky"]
for color, name in zip(colors, names):
    print("The color is", color, "and the name is", name)
