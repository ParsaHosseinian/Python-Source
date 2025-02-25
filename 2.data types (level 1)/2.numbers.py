# in python you may face to something like this:
print(0.1 + 0.2) # we expect the result to be 0.3 but it prints 0.30000000000000004 !!
print(0.1 + 0.2 == 0.3) # and we expect it to be true but it returns false !!
# the reason is in python numbers are saved as binary in computer
# and binary has a little issue about saving float numbers
# for more details search this on the web

# there are lots of solutions for this on web but a good one is:
from decimal import Decimal

x = float(Decimal('0.1') + Decimal('0.2'))
print(x)
print(x == 0.3)
print(type(x))

###############
import fractions # used to represent numbers as fractions
print(fractions.Fraction(1.5))

###############
# in Python, for numbers that have many digits and are difficult to read, you can use "_" to separate
# all three digits of the number to make it easier for the programmer to read,
# but it has no effect on the value of the number.
print(10_000_000_000) # prints 10000000000

###############
# we can also display numbers in scientific notation.
num1 = 1e+7 # 1 * 10 ** +7
print(num1)
print(type(num1)) # and it's type is float

###############
# we can round nubmers by round() function like:
num2 = 1.323423445
print(round(num2, 2)) # prints 1.32

# we can have Absolute value of numbers by abs() function:
num3 = -24
print(abs(num3))

# pow() => with this function, which has two inputs,
# we can raise the first input to the power of the second input.
print(pow(2, 3)) # prints 8