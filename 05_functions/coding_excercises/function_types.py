
# This file will be tested automatically.
# Do not change the function names or parameters.
 
total_sum = 0  # global variable for impure function
 
def pure_add(a: int, b: int) -> int:
    return a + b
 
def impure_increment() -> int:
    global total_sum
    total_sum += 1
    return total_sum
 
def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
 
def square_list(nums: list[int]) -> list[int]:
    return list(map(lambda n: n ** 2, nums))