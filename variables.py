# comment line
# Variables
msg = 'hello python'
message = ' woW I am coding'
num = 123
a = 34
b = 88
c = 1
status = True  # boolean
print(a + b)
print(message)
print(msg, message)
print('hello world')
print(msg, message)
print("python world")
# data types : primitive data type : numbers(integer,double, float), strings, boolean
# data structures: list, dictionary ...
print (type(b)) # print(), type() is the built-in functions
print(type(c))
print(type(message))
print (type(status))

print('******* builtin function ********')
print(message)
print(message.upper())
print(message.lower())
print(message.title())
city = 'brooklyn'
country = 'USA'
print(city,country)
city = '   brooklyn  '
country = '  USA  '
print(city.strip(),country)
print("****** concatination ******")
print('My location is ' + city.strip().title() +',' + country.upper())
print('---special characters tab, new line (enter)')
print('*******\n****\t\t******\n\t*******')
#variable can hold various data types
#lower case, no spaces(new_message), dont start with number
dog='darcy'
top='likes to play with ball'
print(dog,top)
jersey="I live in west new york"
west='before jersey, I was living in brooklyn'
print(jersey,west)
x=45
y=55
print('sum of x and y:', x + y )
x=145
print('2 sum of x and y:', x + y )
num2 = 5
num3 = 3
print('result', 5**3) # expoment: 5*5*5
print('modulo', num2 % num3)
# when you divide number (a) modulo returns  a remainder(c) 5= 3+1 +2  | x = a*b+c
print('floor division',num2 // num3)
#Odd number: 1,3,5 ...(not even number)
#even numbers : 2,4,6.... (dividable by 2)
num3 = 50
print('if modulus 0 then given number is dividuble by 2, so it is even number')
print('remainder:', num3 % 2)
print("************* Useful function while working with numbers ********")
print('regular division, result is float:',100/3)
print('converting division result to integer:',int(100/3))
print('regular division, result is int',100/2)
print('converting division result to a float', float(100/2))
print('******** useful function while working with mix data type')
age = 25
msg1 = 'I am ' + str(age) + ' years old'
print(msg1)
msg1 = f'I am {age} years old'
print(msg1)
# int(45.5), str(n), float(a)
print(25+30) # 55
print('25' + '30') # 2530 we are just combining text values





