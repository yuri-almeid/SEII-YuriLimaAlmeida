

student = {'name': 'Jhon', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
# print(student[1])
print(student.get('phone', 'Not Found'))
student['phone'] = '00 0 0000 0000'
print(student.get('phone', 'Not Found'))
student['name'] = 'Yuri Almeida'
print(student)
student.update({
    'name': 'Jane',
    'age': 26,
    'phone': '99 9 9999 9999',
    'courses': ['Math', 'CompSci']
})
age = student.pop('age')
print(student)
print(age)
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)