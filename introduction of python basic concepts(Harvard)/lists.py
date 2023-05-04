my_empty_list = []
print('empty list: {}, type: {}'.format(my_empty_list, type(my_empty_list)))


list_of_ints = [1, 2, 6, 6, 7]
list_of_misc = [0.2, 5, 'Python', 'is', 'still fun', '!']
print('lengths: {} and {}'.format(len(list_of_ints), len(list_of_misc)))


my_list = ['Python', 'is', 'still', 'cool']
print(my_list[0])
print(my_list[3])


# Checking if certain value is present in list
languages = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
if 'Python' in languages:
    print('Python is there!')


# list.append()
my_list = ['Java', 'C++', 'Go', 'Python', 'JavaScript']
my_list = [1]
print(my_list)
my_list.append('ham')
print(my_list)


my_list = ['Python', 'is', 'still', 'cool']
print(my_list)
print(my_list.pop(0))
print(my_list)


my_list = [3, 4, 1, 0]
my_list.sort()
print(my_list)


my_list_numbers = [3, 4, 1, 0]
my_list_words = ['Python', 'is', 'still', 'cool']
my_list_numbers.extend(my_list_words)
print(my_list_numbers)
print(len(my_list_numbers))


my_list_numbers = [3, 4, 1, 0]
my_list_words = ['Python', 'is', 'still', 'cool']
my_list_numbers.append(my_list_words)

print(my_list_numbers)
print(len(my_list_numbers))


my_list_words = ['Python', 'is', 'still', 'cool']
A = my_list_words
A.extend('!')
print(A)
print("===========")
print(my_list_words)

# the result is:

# ['Python', 'is', 'still', 'cool', '!']
# ===========
# ['Python', 'is', 'still', 'cool', '!']


# You can get around this by creating new list:


original = [1, 2, 3]
modified = list(original)  # Note list() 
# Alternatively, you can use copy method
# modified = original.copy()
modified[0] = 99
print('original: {}, modified: {}'.format(original, modified))