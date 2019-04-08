from sys import getrefcount
h = 'hello'
print(getrefcount('hello'))
a = 'hello'
print(getrefcount('hello'))
b = a
print(getrefcount('hello'))
c = b
print(getrefcount('hello'))
del b
print(getrefcount('hello'))
del c
print(getrefcount('hello'))
del a
print(getrefcount('hello'))
