# Basically it does whatever follows 5 times.
# The "i" - a variable that helps us keep track where we are in a loop. 
for i in range(5):
    print ("python")

print("==========")

t = [0, 1, 2, 3, 4]
for i in range(5):
    print ("python", i)


my_list = [1, 2, 3, 4, 'Python', 'is', 'neat']
for item in my_list:
    print(item)


# Break
#      stop the execution of the loop

for item in my_list:
    if item == 'Python':
        break
    print(item)


for number in range(5):
    print(number)


for number in range(2, 5):
    print(number)


for number in range(0, 10, 2):  # last one is step
    print(number)
    