#матрица
def get_matrix (n, m, value):
    matrix = [] # оздайте пустой список matrix внутри функции get_matrix
    for i in range (n): #первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        hhh = []  # добавляйте пустой список в список matrix.
        matrix.append(hhh)
        for j in range (m): # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            hhh.append(value) # пополняйте ранее добавленный пустой список значениями value
    return matrix # всех циклов верните значение переменной matrix

result1 = get_matrix (2, 2, 10) # 2 раза "10" в каждом списке
result2 = get_matrix(3, 5, 42) # 3 раза по 5 "42"
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)



