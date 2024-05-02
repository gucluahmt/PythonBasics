print(' Welcome you have choice of 3 toppings for ice cream ')
topping1 = input('please enter your first choice of ice cream topping :')
topping2 = input('please enter your second choice of ice cream topping: ')
topping3 = input('please enter you third choice of ice cream topping: ')
print(f'you have entered: {topping1}')
print(f'you have entered: {topping2}')
print(f'you have a entered: {topping3}')
print('------we started making your ice cream------')
available_toppings = ['chocolate', 'vanilla', 'strawberry', 'peanut']
requested_toppings = [topping1, topping2, topping3]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print( 'Adding ' + requested_topping + '!')
    else:
        print("Sorry we dont have " + requested_topping + "!")
print('finished making your ice cream')


