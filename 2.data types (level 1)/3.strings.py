# isinstance function: with it, we check whether our variable is of the type we want.
number1 = 2
print(isinstance(number1, int)) # checks if number1 is integer or not

str1 = 'I\'m parsa' # we use \ between I and m so that python won't confuse about quotations arrangements
str2 = 'I am \n parsa' # characters after \n are printed on the next line.
str3 = 'test \t string' # there is a tab-sized gap between the test and the string.
str4 = 'C:\Downloads\new' # it prints C:\Downloads
#                                     ew
# there are two ways to fix the above issue
# way 1:
str4fixed1 = 'C:\Downloads\\new' # prints C:\Downloads\new (the responde that we expect)
# way 2:
str4fixed2 = r'C:\Downloads\new' # prints C:\Downloads\new (the responde that we expect)

str5 = """ 
parsa
Hosseii
computer
code

python
""" # prints exactly like str5 structure in the source code.
print(str1)
print(str2)
print(str3)
print(str4)
print(str4fixed1)
print(str4fixed2)
print(str5) 

print('parsa ' + 'hosseii') # parsa hosseii
print(5 * 'parsa ' + 'hosseii') # parsa parsa parsa parsa parsa hosseii

str6 = "parsa hosseii"
print(str6[1]) # prints index 1 of the string: a
print(str6[2:-2]) # prints => rsa hossei => from index 2 to -2
print(str6[:-2]) # prints => parsa hossei => from index 0 to -2
print(str6[0:5] + str6[5:]) # prints => parsa hosseii => all the chars
print(str6[::2]) # => one prints out the characters
print(len(str6)) # => returns the length of the string
print(str6[::-1]) # => returns the reverse string 
