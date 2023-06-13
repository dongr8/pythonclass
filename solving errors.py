Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> for i in range(9)
SyntaxError: incomplete input
>>> 
>>> 
>>> print(x)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> 
>>> 
>>> x = {"a":1212, "b":"abds", "c":"KLJH"}
>>> print("d")
d
>>> d
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> print(x[d])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(x[d])
NameError: name 'd' is not defined. Did you mean: 'id'?
