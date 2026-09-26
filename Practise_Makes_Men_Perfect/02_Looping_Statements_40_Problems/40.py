# Exercise 40. Nested list search (2D matrix coordinates)
# Practice Problem: Given a 2D list (matrix), find the row and column index of a target value.

matrix = [[10, 20], [30, 40], [50, 60]]
target = 50

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]==target:
            print(i,j)

for index_1,data_1 in enumerate(matrix):
    for index_2,data_2 in enumerate(data_1):
        if data_2==target:
            print(index_1,index_2)
            break