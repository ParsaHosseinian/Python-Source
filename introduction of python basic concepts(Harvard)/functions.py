# Imagine a function as a machine with three parts.
# First, there's the "input"
# The input is the parameter to the function
# The second part is the body of the function. This is
# where the function does something to the input
# And lastly, there's the return statement. This
# is where the function outputs the result

# For example, take a sandwich-making machine.
# The input would be the list of topings. For example, it may
# take inputs like ["cheese", "ham", "lettuce"]
# The body of the function involves actually making the sandwich
# by putting together the input (the ingredients) with
# bread and other condiments.
# Finally, the machine "returns" or serves the sandwich

# This is what a function looks like in Python
def add(x, y):
    result = x + y
    return result

print (add(2, 2))



#without return value
def greet_us(name1, name2):
    print('Hello {} and {}!'.format(name1, name2))

greet_us('John Doe', 'Superman')



def my_fancy_calculation(first, second, third):
    """
    this is test
    """
    return first + second - third 

print(my_fancy_calculation(3, 2, 1))

print(my_fancy_calculation(first=3, second=2, third=1))

# With keyword arguments you can mix the order
print(my_fancy_calculation(third=1, first=3, second=2))
