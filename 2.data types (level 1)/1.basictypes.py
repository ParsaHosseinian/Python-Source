# First off, let's start with the basic basics. In Python, each object /
# thing has a type.

print ("Hello World!") # This is a string
print (3) # This is an integer
print (4.5) # This is a float - a number with a decimal point
print ("I am", 50, "years old") # We can print multiple things by separating by commas

# We can check the type of an object using the type() 
print (type("Hello World!")) #"str" means string
print (type(3)) #"int" means integer
print (type(4.5)) #"float" means a number with a decimal

# Another basic type in Python is the boolean. 
# It can be used with logical operators like AND or OR

print (True and False) # This is False
print (True or False)  # This is True
print (True and True)  # This is True
print (False or False) # This is False
print("===========")

print('1 == 0: {}'.format(1 == 0))

print('1 != 0: {}'.format(1 != 0))
print('1 > 0: {}'.format(1 > 0))
print('1 > 1: {}'.format(1 > 1))

print('1 >= 0: {}'.format(1 >= 0))
print('1 >= 1: {}'.format(1 >= 1))


# Dictionary
myDict = {"parsa": "beautiful", "x": 5}
print(type(myDict))

# Set - like a set of numbers
mySet = {1, 2, 3, 4, 4, 6,}
print(mySet)
print(type(mySet))

# Sequence type => String, List, Tuple : we can do for loop them
# String:
me = "Parsa Hosseii"
print(me[2:4])

# Tuple:
myTuple = (1, 2, 3, 4, 5)
print(myTuple[2:4])

# List:
myList = [1, 2, 3, 4, 5]
print(myList[2:4])

#########

#Special => None
x = None
print(type(x)) # prints "nonetype"