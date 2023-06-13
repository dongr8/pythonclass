import random

print("t\t\t Welcome to my Code")

flipped_coin = int(input("enter number of flipped coins"))

number_tail = int(input("enter number of tail"))

number_tail = flipped_coin - number_tail

no_of_heads = random.randrange(10)+20

flipped_coin = 90 #note that the prevalue can be stringed

while flipped_coin != no_of_heads | number_tail:
    flipped_coin = quit
    print("Oh! am really sorry")
    print("The number of times the coin flipped is", flipped_coin)
    print("The number of heads recorded are", no_of_heads)
    print("The number of tails recorded are", number_tail)

    

    if flipped_coin != "no_of_heads":
        print("\n\n\t\tCool though number of  coins not equal to Heads")
        if flipped_coin != "number_tail":
            print("\n\n\t\t number of heads is equal to number of ")
            
            input("Press enter to end the program:")
            flipped_coin = no_of_heads | number_tail
    

import hashlib

with open("C:\\Users\\Charis\\Documents\\AUGUST 2022 VI NURSES ROTA.docx","rb")as file:
    data = file.read()

hash_value = hashlib.sha1(data).hexdigest()

print(hash_value)
