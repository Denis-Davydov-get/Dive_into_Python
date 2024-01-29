# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix,
# и возвращает транспонированную матрицу.
# Input:
matrix = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# Output:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
def transposition_matrix(matrix):
    result_matrix = [[],[],[]]
    for i in range(len(matrix)):
        for k in range(len(matrix)):
            result_matrix[i][k] = matrix[i][k] + matrix[i][k]

print(transposition_matrix(matrix))