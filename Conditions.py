
#Working with IF Condition

x = 5
if x > 0:
    print("X is Positive")
else:
    print("X is Negative")

X = 10
if X > 0:
    print("X is greater than 0")

men = 20
women = 30
if men >= 20:
    print("men are not more than 20")
else:
    print("Men are greater than 20")

if women <= 30:
    print("women are less than 30")
else:
    print("women are more than 30")

#Checking if number is positive

B = 5
if B > 0:
    print("B is Positive")
else:
    print("B is Negative")


#Checking if number is even

X = 8
if X % 2 == 0:
    print("X is Even")
else:
    print("X is negative")


Y = 7
if Y % 2 == 0:
    print("Y is Postive")
else:
    print("Y is Negative")


#Checking if a string is empty

S = ""
if not S:
    print("string is empty")
else:
    print("string is empty")


#Checking if an element is in a list

F = [1, 2, 3, 4, 5]
H = 3
if H in F:
    print("H is in the list")
else:
    print("H is not in d list")


G = 6
if G in F:
    print("G is in d list")
else:
    print("G is not in d list")


lst = [2, 3, 2, 33, 4, 5, 6, 43, 20, 2, 3, 6, 8]
K = 55
A = 32
if A in lst:
    print("A not in Lst")
else:
    print("A in lst")

if K in lst:
    print("K is in lst")
else:
    print("k is not in lst")


dct = {"a":1, "b":2, "c":3}
key = "b"
if key in dct:
    print("key in dct")
else:
    print("key not in dct")

X = 12
if isinstance(X, int):
    print("X is an integer")
else:
    print("X is not an integer")


D = 5
if D >= 1 and X <= 10:
    print("D is within the range")
else:
    print("D not within the range")


X = 5
if X > 0:
    print("X is positive")
elif X < 0:
    print("X is negative")
else:
    print("X is zero")
