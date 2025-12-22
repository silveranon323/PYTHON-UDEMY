# 1. List comphrension
# instead of using for loop we can use comphrension to add value into the list
# [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5]
squares= [number*number for number in numbers]
print(squares)

# dictionary comphrension
# syntax : {keyexpression: value_expression  for item in iterable if condition}
# key_expression=expression to generate keys
# value_expression: expression to generate_values

numbers = [1,2,3,4]
# storing each number as key and their 2x square as value

squares_dict={n:n**2 for n in numbers}
print(squares_dict)