# We can document in two ways:
# 1.comment: this line is a one line comment.
# 2.docstring: For example, at the beginning of a function or class,
# we write it, which gives an explanation about that function or class.
def F():
    """ this function prints my name """ #=> this is one line docstring
    
    print("Parsa")

# interpreter ignores executing comments and they are just for documenting notes and tip about code
# in the source code to guide programmers.
#
# Unlike a comment, a docstring is not ignored by the interpreter:
print(F.__doc__) #=> this returns F function docstring
#
# Unlike a comment, a docstring is not a guide for programmers but it is a guide for who that wants to use the codes.
