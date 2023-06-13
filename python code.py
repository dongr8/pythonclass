txt = 'I am a \'good\' boy'
txt = 'I am a good boy'
print(txt.strip())


age = 36
txt = 'my name is john, and i an {}'
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = 'i want {} pieces of item {} for {} dollars.'
print(myorder.format(quantity, itemno, price))
