print('Task: 1')
print()

print(int(234))
print(float(43.23))
print(complex((4-1j)))
print(str('Hello'))
print(bool('true'))



print()
print('Task: 2')
print()

print(float(43.12),' is type of ',type(43.12))
print((4-1j), 'is type of ',type((4-1j)))
print(str('Hey whats up dude?'), type('yo'),sep= 'is type of')
print(bool('true'),type(bool('true')),sep=' is type of')
print()
print('Task: 3')
print()


print(isinstance(123,int))
print(isinstance(43.23,str))
print(isinstance(True,bool))
print(isinstance(4-1j,complex))
print(isinstance('city',int))

print()
print('Task: 4')
print()

print('Is 123 an instance of int?: ', isinstance(123,int) )
print('Is 43.23 an instance of bool: ', isinstance(43.23,bool) )
print('Is (4-1j) an instance of complex: ', isinstance((4-1j),complex) )
print('Is True an instance of bool: ', isinstance(bool('true'),bool) )
print("Is 'How are you?' an instance of float: ", isinstance('lol',float) )

print()
print('Task: 5')
print()

# This is my first comment
# Block comments are indented to the same level as that code

print("Hello")
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number

"""
You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""
