# useful string methods
str1 = 'parsa-hosseii'
print(len(str1)) # len() is not a method but a function
print(str1.upper()) # the entire string is converted to uppercase
print(str1.lower()) # the entire string is converted to lowercase
print(str1.count('s')) # counts how many s str1 has 
print(str1.endswith('s')) # checks if str1 ends with s or not - returns boolean (True or False)
print(str1.startswith('s')) # check if str1 starts with s or not - returns boolean (True or False)
print(str1.find('s')) # returns index of the first s in str1 if it is found
print(str1.rfind('s')) # returns index of the last s in str1 if it is found
print(str1.isalnum()) # checks whether str1 consists entirely of numbers or strings
print(str1.isnumeric()) # checks whether str1 consists entirely of numbers

seperator = '-'
list = ['p', 'a', 'r', 's', 'a']
print(seperator.join(list)) # prints p-a-r-s-a

# spliting the string:
print(str1.split('-')) # returns ['parsa', 'hosseii']

print(str1.replace('s', '*')) # replaces all s chars with *

# strip method
str2 = "                 parsa hosseii               "
print(str2.strip()) # removes spaces before and after the string
str3 = "+++parsa hosseii+++++"
print(str3.strip('+')) # removes all + before and after the string
print(str3.lstrip('+')) # removes all + only before the string
print(str3.rstrip('+')) # removes all + only after the string

print(str1.capitalize()) # returns the string with the first letter capitalized