# In Python, we can store objects in variables.
# they can hold some sort of value which we can access and change anytime we want

greetings = "Hello World"
print (greetings)

name = "Parsa"
print ("My name is", name)

age = 80
print ("I am", age, "years old")

hungry = True
thirsty = True
print (hungry and thirsty) # prints True

print(4, 2, 5, 8, sep=", ") # prints 4, 2, 5, 8 (seperated by ', ')

print(4, end="-") # prints - after 4 and before next line print() executes, instead of inserting a line (\n).
print(end="-")
print(end="-")
print(5, end="-")
# Result of the 4 lines above: 4---5-

username = input("Enter your name: ") #now user can enter their name as an input of this program.
print("your name is:", username)