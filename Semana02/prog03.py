# Lista inicial
courses = ['Math', 'Physics', 'History', 'CompSci']
# Manipulaçao de listas
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[1:])
courses.append("Art")
print(courses)
courses.insert(-1, "Geography")
print(courses)
courses_1 = []
courses_2 = ["Chemical", "Spanish"]
courses_1.extend(courses)
courses_1.insert(0, courses_2)
print(courses_1)
courses.extend(courses_2)
print(courses)
courses.remove("Spanish")
print(courses)
popped = courses.pop()
print(courses)
print(popped)
courses.reverse()
print(courses)
courses.sort()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nums.sort()
print(courses)
print(nums)
nums.sort(reverse=True)
sorted_courses = sorted(courses)
print(nums)
print(sorted_courses)
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.index("CompSci"))
print("Art" in courses)
for index, course in enumerate(courses, start=0):
    print(index, course)
course_str = ' - '.join(courses)
print(course_str)
new_list = course_str.split(' - ')
print(new_list)
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
print(tuple_1)
print(tuple_2)
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'Math', 'Art', 'Design', 'History'}
print(cs_courses)
print(art_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = {} 
empty_set = set()
