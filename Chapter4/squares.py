
squares = [ ]
for value in range(1,11):
    square = value**2  #** represents exponents
    squares.append(square)

print(square)

##List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)