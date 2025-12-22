myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
sum_of_diagonals=0
for i in range(len(myList2D)):
    sum_of_diagonals+=myList2D[i][i]
print(sum_of_diagonals)