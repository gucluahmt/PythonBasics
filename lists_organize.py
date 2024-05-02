cars = ["ferrari", "maybach", "tesla", "audi"]
nums = [4, 6, 2, 11, 3, -55]
print('*********permanent sorting ******')
cars.sort() #  sorting to original list ascending order alphabeticly. it does not return you copy
nums.sort() #  sorting to original list ascending order alphabeticly

print("permanent asc sorted cars",cars)
print("permanent ascending sorted nums",nums)
cars1 = ["ferrari1", "maybach1", "lambo2", "tesla1", "audi1"]
nums1 = [14, 16, 12, 111, 12, 13, -155]

cars1.sort(reverse=True) #  sorting to original list descendin order alphabeticly
nums1.sort(reverse=True) #  sorting to original list descending order alphabeticly

print("permanent reverse sorted cars1",cars1)
print("permanent reverse sorted nums1",nums1)

print('********temporary sorting ******')
cars2 = ["ferrari2", "maybach2", "lambo2", "tesla2", "audi2"]
sorted_cars2 = sorted(cars2) # returns the new copy of the list
print('original cars2',cars2)
print('sorted copy of cars2',sorted_cars2)
