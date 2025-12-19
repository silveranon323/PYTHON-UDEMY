a=10
b=5
try:
    result=a//b
except ZeroDivisionError:
    print("Zero division error.")
else:
    print("The result is" , result)