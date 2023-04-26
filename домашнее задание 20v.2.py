import random

y = int(input("y = ")) #размер матрицы по оси у
x = int(input("x = ")) #размер матрицы по оси х

#создаем первую матрицу
matrix_1 = [[random.randint(1, 11) for j in range(x)] for i in range(y)]
print("Matrix 1: ")
for i in range(y):
    print(matrix_1[i])

#создаем вторую матрицу
matrix_2 = [[random.randint(1, 11) for j in range(x)] for i in range(y)]
print("Matrix 2: ")
for i in range(y):
    print(matrix_2[2])

#сложение двух матриц
result = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Результат суммы двух матриц: ")
for z in result:
    print(z)
