# Data Structures: List (Array), Dictionary (Hashmap), Set, Tuple (last 2 just slightly)
# what do I need to know about data structures: CRUD operations
# Create
# Access (Read)
# Update
# Delete
# Loop: repetitive actions on the DS,loop through whole DT, loop through partially
# Conditions: If Statements
# list : [elem1, elem2, ..., elemN]
# indexing starting with 0, 1, 2 ...
#Indexing with negative numbers : -1(elemN), -2(elem-1)..
print('***********Creating a LIST ********')
numbers = []
students = ['alex','ali','anna','elvin']
cities = list((45, 55, 666))  # creates and converts iterative objects (sets, dictionary,range(),...)
print(cities)
print(students)

print('*********** Accessing th list with index *******')
print('second student in the list', students[1])
print(f'second student in the list:, "{students[1]}".')
print(f'Last student in the list:, "{students[3]}".')
print(f'Last student in the list:, "{students[-1]}".')

print('********** Update the list element VALUES *******')
# update alex to alexander
students[0] = 'Alexander'
print(f'whole list:{students}')
print(f'first student name:{students[0]}')

print('********** Update: Modifying Values to the list *********')

print('-----Adding the values to the end of the list(mostly done)  ---- ')
students.append("stela")
print(f'whole list:{students}')
print('-----Adding a value to any position(index) of the list----')
students.insert(1,'mansur')
print(f'updated list, inserted mansur to the list:{students}')

print('------Deleting the value to the list -------')
print('**** Deleting the element with del function ****')
del students[4]
print(f'updated list, deleted elvin to the list:{students}')
print('-----Deleting element with pop() function ----')
students.pop() # deletes the last element by default, when no arguments passed
print(f'updated list, pop() default:{students}')
students.pop(3)  #deletes the element at index 3 anna
print(f'updated list, pop(3) default:{students}')
students.insert(1,'ali')
print(f'updated list, inserted ali to the list:{students}')
print('-----deleting the element with remove()-----')
students.remove('ali')   #removes only first ali
print(f"updated list, deleted by value 'ali' from the list: {students}")


