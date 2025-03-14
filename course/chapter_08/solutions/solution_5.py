# Исходная матрица
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
tmatrix = []
for j in range(len(matrix[0])):
    new_row = [] 
    for i in range(len(matrix)):
        new_row.append(matrix[i][j])
    tmatrix.append(new_row)  
    print(" ".join(map(str, new_row)))
