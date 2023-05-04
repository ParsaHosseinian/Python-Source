# Kind of like your ordinary dictionary, you have two main
# parts - the key and the value. In an actual dictionary,
# this is equivalent to the word and its definition.

dict1 = {'value1': 1.6, 'value2': 10, 'name': 'John Doe'}
dict2 = dict(value1=1.6, value2=10, name='John Doe')

print(dict1)
print(dict2)

print('equal: {}'.format(dict1 == dict2))
print('length: {}'.format(len(dict1)))



print('keys: {}'.format(dict1.keys()))
print('values: {}'.format(dict1.values()))
print('items: {}'.format(dict1.items()))


my_dict = {}
my_dict['key1'] = 'value1'
my_dict['key2'] = 99
my_dict['key1'] = 'new value'  # overriding existing value
print(my_dict)
print('value of key1: {}'.format(my_dict['key1']))



my_dict = {'key1': 'value1', 'key2': 99, 'keyX': 'valueX'}
del my_dict['keyX']
print(my_dict)

# Usually better to make sure that the key exists (see also pop() and popitem())
key_to_delete = 'my_key'
if key_to_delete in my_dict:
    del my_dict[key_to_delete]
else:
    print('{key} is not in {dictionary}'.format(key=key_to_delete, dictionary=my_dict))



my_dict = {'a': 1, 'b': 2, 'c': 3}
d = my_dict.get('d')
print('d: {}'.format(d))

d = my_dict.get('d', 'my default value')
print('d: {}'.format(d))