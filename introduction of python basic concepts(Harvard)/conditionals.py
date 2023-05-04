statement = True

if statement:
    print('statement is True')

if not statement:
    print('statement is not True')

statement = True
if not statement:
    print('if')
else:
    print('else')

greeting = 'Hello fellow Pythonista!'
language = 'Italian'

if language == 'Swedish':
    greeting = 'Hejsan!'
elif language == 'Finnish':
    greeting = 'Latua perkele!'
elif language == 'Spanish':
    greeting = 'Hola!'
elif language == 'German':
    greeting = 'Guten Tag!'
    
print(greeting)