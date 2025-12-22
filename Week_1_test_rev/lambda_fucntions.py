# lambda arguments:expresssions

square = lambda x : x**2
square(10)
print(square(4))

# map this is used to apply a function to each item present in a iterable

# map(function,iterable) here this function can also be a lambda expression

numbers=[1,2,3,4]
result=list(map(lambda x : x**2 , numbers))
print(result)

# filter function: used to filter group of data based on a function
# filter(function,iterable)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers=list(filter(lambda x : x%2==0,numbers))
print(even_numbers)