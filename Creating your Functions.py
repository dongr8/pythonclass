def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


def more(fname, lname):
    print(f"Hi {fname} {lname},")
    print("Welcome aboard")


more("Smith", "Doe")
    

#Two Types of Functions
# 1 Performs a Task
# 2 Returns a Value
#eg def greet(name):
    #print(f"Hi{name}")

#round(1.9)

def get_greet(name):
    return f"Hi {name}"

message = get_greet("James")
print(message)

def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

print(increment(2, 1))

print(increment(2, by=1))

def increment(number, by=1):
    return number + by

print(increment(6, 2))


def multiply(num1, num2 ):
    return num1 * num2

print(multiply(2, 2))

total = multiply(2, 2)
print(total)


def multiply(*numbers):
    total =1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

sum = multiply(2, 3, 4, 5)

print(sum)


def save_user(**user):
    print(user)


save_user(ID=1, Name="John", Age=30, Email="luckcharis@gmail.com")



def fizz_buzz(input):
    if (input % 3 ==0) and (input % 5 ==0):
        return "fizz_buzz"
    if input % 3 ==0:
        return "fizz"
    if input % 5 ==0:
        return "buzz"
    return input


print(fizz_buzz(7))


 
    
    
















































    

