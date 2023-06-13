response = "" #true
while response != "Because": #You must enter Because to break the loop or pass.
    response = input("Enter a value:")
    print("Pass if you get it right")

print('::::::::::::::::::::::::')

#Build a dictionary containing everything we know about a user.
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
        return profile

user_profile1 = build_profile('alamin', 'jasmin', location = 'Ikeja', field = 'computer science')
print(user_profile1)

print('::::::::::::::::::::::::')

person = {"name": "Charis", "age": 30, "address": "Nigeria"}

print(person["age"])
print(person["address"])
print(person["name"])
person["age"] = 50
print(person)
person.get("age")
print(person["age"])


































