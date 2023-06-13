
shopping_list =["Apple", "Orange", "Banana","Apple", "Mango"]
Tinubu = ["MC Oloumo", "jalo", "Rufai"]
print(shopping_list)
shopping_list.append("agbado")
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.insert(3, "agbado")
print(shopping_list)
shopping_list.remove("Orange")
print(shopping_list)
shopping_list.reverse()
print(shopping_list)
x = shopping_list.count("Apple")
print(x)
print(shopping_list.count("Apple"))
print(shopping_list.copy())
chidinma = shopping_list.copy()
print(chidinma)
shopping_list.sort()
print(shopping_list)
shopping_list.sort(reverse=True)
print(shopping_list)
shopping_list.sort(reverse=False)
print(shopping_list)
print(shopping_list.index("Banana"))
shopping_list.extend(Tinubu)
print(shopping_list)


print("""
    ### #  # ##### ##### #####
    ##   ##  ##  # ##    ##  #
    ##   ##  ##### ##### #####
    ##   ##  ##  # ##    ####
    ###  ##  ##### ##### ##  ##
    """)

      
cyber = ["cloud","hardware","operational","end user", "quantum", "IOT","IOE",
           "application", "web","data"]

print(cyber.index("cloud"))
print(cyber.count("cloud"))
cyber.append("design")
print(cyber)
cyber.pop()
print(cyber)
cyber.insert(2, "Computer")
print(cyber)
cyber.sort(reverse=True)
print(cyber)
cyber.sort(reverse=False)
print(cyber)
print(cyber.copy())
cyber.remove("web")
print(cyber)










