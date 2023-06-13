
#Functions in Python

#Determine Voting Age

def canVote(Age):
    if Age >= 18:
        return "yes"
    else:
        return "no"

result = canVote(23)
print(result)

def can_vote(age):
    if age >= 18:
        return "yes"

    return "no"
outcome = can_vote(23)
print(outcome)


def votingAge(age):
    return "Yes" if age >=18 else "No"

vote = votingAge(17)
print(vote)

#Converting IF/ELSE STATEMENT INTO DICTIONARY

def do_one(X):
    print("one: X*1 = ", X*1)

def do_two(X):
    print("two: X*1 = ", X*2)

def do_three(X):
    print("three: X*3 = ", X*3)

def do_default(X):
    print("default: X = ", X)


X = 3

if X ==1:
    do_one(X)
elif X == 2:
    do_two(X)
elif X ==3:
    do_three(X)
else:
    do_default(X)

actions = {1: do_one, 2:do_two, 3:do_three}

action = actions.get(X, do_default)
action(X)


x = 2

def num1(x):
    print("num1: x*1 = ", x*1)

def num2(x):
    print("num2: x*2 =", x*2)

def num3(x):
    print("num3: x*3 = ", x*3)

def num(x):
    print("num: x = ", x)

numbers = {1:num1,2:num2, 3:num3}
number = numbers.get(x, num)

number(x)



























    

