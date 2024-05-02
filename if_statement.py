cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw' :
        print('this is the real beast:', car.upper())

    else:
        print(car.title())
 # car == 'bmw' ~> comparing the value(bmw or not) , expression returns true or false
 #car = 'bmw' # assigning the value to car variable

  #Expressions that return true or False, can be use in the if statement

 #True, False
 #2<3 (true)
 #num <5 , num num >10
 # 'tesla' in cars >false/true

nums =[ 3, 6, 1, 10, 6]
 # print'I got number' whenever you find number 6 in the list
 # if you dont find number 6 then just print 'next'
for num in nums:
     if num == 6:
         print('I got the number:', num)
     else:
         print('next')

