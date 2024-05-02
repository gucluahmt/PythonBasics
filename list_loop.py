# Looping

magicians = ['elise', 'david', 'carolina']

for magician in magicians:
    print(magician)
    print('***** this is repeatable line*****')

nums = [3, 5, 1, 8]
#print list of square of these numbers
squares = [] #mutable can be changed
coordinates = (10, 30) # tuple: immutable: you can not change
for i in nums:
    print('calculating the square:',i)
    #print(i**2)
    squares.append(i**2)
print(squares)
cars = ['tesla', 'merc', 'toyota', 'rols']
for car in cars:
    print(f'i love my {car}!')
    print('******** end of the dream*****')
print('********* exercise 4.1 *****not pizza but kebab******')
kebabs = ['chicken','shish', 'adana', 'lamb']
for kebab in kebabs:
    print(f'i like {kebab} kebab')
print('I love having kebabs for lunch from greece restaurants')



