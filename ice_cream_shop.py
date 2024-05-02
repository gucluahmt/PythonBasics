print('Welcome to our ice cream shop')
print('you have choice of 3 toppings')
topping1 = input('please enter your first choice: ')
topping2 = input('please enter your second choice: ')
topping3 = input('please enter your third choice: ')

print(f'You have entered {topping1} !')
print(f'you have entered {topping2} !')
print(f'you have entered {topping3} !')

available_toppings = ['chocolate', 'vanilla', 'strawberry', 'caramel']
requested_toppings = [topping1, topping2, topping3]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '!')
        print(" Sorry we don't have " + requested_topping + "!")
        print('would you like to continue? Yes or No')
        input('')
    else:
        input(f'please enter your choice: ')



print('finished making your ice cream ')
