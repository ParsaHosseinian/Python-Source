# there are two types of lines:
# 1.physical lines: each line is numbered, which can be seen in the code editor.
# 2.logical lines: any part of the code that the interpreter considers a logical line and can be separated
#  into a physical line by ';'.
y = 2 + 2; z = 12 + 4; str = "hello world";

# we can seperate a logical line in python by '\' into several physical lines.
x = 7 + 8 + 4 + \
    7 + 8 + 4 +\
    7 + 8 + 4\
    + 7 + 8 + 4

print(x)