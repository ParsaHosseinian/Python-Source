# identity-operators

# is 
# returns true if the both variables are the same object

# is not 
# returns true if the both variables are not the same object

# little tip:

x = [1, 2, 4]
y = [1, 2, 4]
print(x is y) # returns false
# but: 
a = 3
b = 3
print(a is b) # returns true

# so if we get their id we understand the reason of the result differences:
print("list x id:", id(x))
print("list y id:", id(y))
print("number a id:", id(a))
print("number b id:", id(b))

# so we know that is and is not check their ids