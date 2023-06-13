
#We use class to create object.

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

c = Customer("John", "Gold")
print(c.name, c.membership_type)

c2 = Customer("Charis", "Premium")
print(c2.name, c2.membership_type)

c3 = Customer("Books", "Business")
print(c3.name, c3.membership_type)

#Customer = [c, c2] this can still work, but not the approprate way
#For it to work, create another variable or put the two arguements
#in a new variable

customers = [Customer("John", "Gold"), Customer("Charis", "Premium")]

print(customers[1].membership_type)



class Client:
    def __init__(self, name, position):
        self.name = name
        self.position = position

outcome = Client("Gloria", "manager")
print(outcome.name, outcome.position)


class Group():
    def __init__(self, age, name, address, state, country):
        self.age = age
        self.name = name
        self.address = address
        self.state = state
        self.country = country

detail = Group("I am 35,", "My name is Doe,", "I reside at no 4, Calistus Street", "Delta State,", "Nigeria.")
print(detail.age, detail.name, detail.address, detail.state, detail.country)

detail2 = Group(55, "Micheal", "4 Broad street", "Delta state", "Nigeria")
print(detail2.age, detail2.name, detail2.address, detail2.state, detail2.country)

Group = [detail, detail2]
print(detail.name)
print(detail2.address)


class Office:
    def __init__(self, branch, state):
        self.branch = branch
        self.state = state

d = Office("Isolo,", "Oke-Afa, Lagos")
print(d.branch, d.state)


class member: 
    def __init__ (self, advert, frequency):
        self.advert = advert
        self.frequency = frequency
f = member("published", "Monthly")

print(f.advert, f.frequency)



























