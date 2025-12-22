nums = [10, 5, 20, 8, 15]
largest_number=-1
second_largest_number=-1
for num in nums:
    if num>largest_number:
        largest_number=num
    elif num<largest_number and num>second_largest_number:
        second_largest_number=num
print("The second larges number is" , second_largest_number)