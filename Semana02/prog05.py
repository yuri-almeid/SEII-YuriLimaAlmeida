
language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'JavaScript':
    print('Language is Java')
elif language == 'JavaScript':
    print('Language is JavaScript')
else:
    print('No match')




user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad Creds')




user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad Creds')



user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Welcome')




a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(id(a))
print(id(b))
print(a is b)
b = a
print(id(a))
print(id(b))
print(a is b)



condition = False
if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')

