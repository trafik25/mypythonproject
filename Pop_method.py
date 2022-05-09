
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
print("My favorite fruit growing up was " + fruits.pop(1))

###### New Line
fruits = ['apple', 'banana', 'cherry']

my_fav = fruits.pop(0)
print("My favorite fruit growing up was " + my_fav.title())

#### New Line
cars = ['bmw', 'ferrari', 'buick']

best_car = cars.pop(1)
print("My favorite car growing up was " + best_car.title())


####New line--grabs the last value in the list
cars = ['bmw', 'ferrari', 'buick']

best_car = cars.pop()
print("My favorite car growing up was " + best_car.title())