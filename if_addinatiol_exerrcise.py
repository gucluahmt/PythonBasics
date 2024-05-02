friends = [5, 11, 33, 6, 67, 43, 10, 9, 13, 56, 75, 90]
for num in friends:
    if num < 15:
        print('that is what we need')
    elif num < 35:
        print('maybe')
    else:
        print('noooooo')


print('&******** NESTY EXAMPLES******************')
foods = ['kebab', 'lahmacun', 'doner', 'pide']
drinks= ['ayran', 'kola', 'salgam', 'cay']
for food in foods:
    for drink in drinks:
        print(f'iste size {food},{drink} afiyet olsun')

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f'I have a {animal_type}. ')
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('dog','darcy')  #Positional argument we need make sure we provide the arguments in the right order(siralamaya dikkat)
describe_pet('dog','prince') #Fuction needs 2 arguments

def describes_city(city,country):
    """Display information about city"""
    print(f'I live in {city.title()}.')
    print(f'I live in {city.title()} which is capital of {country.title()}')

describes_city('istanbul','turkey')

def make_shirt(size, message):
    """"Make a shirt with a message"""
    print(f'I need a size {size.upper()} the T-shirt that says {message.upper()}')

make_shirt('L', 'I love python')
make_shirt('M', 'I am a best coder')

def describe_person(personality, phsical):
    """describe personality"""
    print(f'I am super honest {personality.upper()} and fit guy {phsical.upper()} ')

describe_person('smart','tall' )
describe_person('patient', 'short')



def describe_city(view, weather):
    print(f'I love view of {view.upper()} and weather is really {weather.title()}')

describe_city('New york', 'cooller')
describe_city('new jersey', 'hot')



#message = input('hello world ')
#print(message)

age = input('please enter your age:')
age = int(age)
if age < 18:
    print('/n sorry you can not order')
else:
    print('/n welcome')



