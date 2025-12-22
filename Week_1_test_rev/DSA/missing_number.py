def missing_number(arr):
    n=max(arr)
    total_sum=sum(arr)
    natural_sum=n*(n+1)//2
    return natural_sum-total_sum
number=[1,2,3,5,6]
print(f"The missing number is {missing_number(number)}")
