for num in range(1,5): #generate number starting from 1, up to 5 incrementing by 1
    print(num)

print('******** range(10) ***********')
for num in range(10):  #starting from 0 up to 10, incrementing by 1
    print(num, end="\t")

print('\n ************ range(5,30, 3 ****** ')
for num in range(5, 30, 3):          #starting from 5 up to 30 incrementing by 3
    print(num, end='\t')

print('*******print squares of even numbers from 10 to 20 *****')
print('even numbers:',end='\t')
squares = []
for num in range(10, 21, 2):
    print(num**2, end='\t')
    squares.append(num**2)

print('******* find min and max from the given unsorted list using min or max function*******')



