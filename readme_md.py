print('welcome, you have 2 choice of topping')
topping2 = input('please enter your first topping: ')
topping22 = input('please enter your second topping: ')
print(f"you have a entered: {topping2}")
print(f"you have a entered: {topping22}")

available_topping = ['sucuk', 'zeytin', 'domates']
requested_toppings = [topping2, topping22]
for requested_topping in requested_toppings:
    if requested_topping in available_topping:
        print('adding ' + requested_topping + '!')
        print('finished making your pizza ')

    else:
        print('sorry, we dont have ' + requested_topping + '!')








