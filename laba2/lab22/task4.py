def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

matrix = []
rows = int(input("Введите количество строк: "))
for i in range(rows):
    row = list(map(int, input(f"Введите элементы строки {i+1} через пробел: ").split()))
    matrix.append(row)

transposed_matrix = transpose_matrix(matrix)

print("\nТранспонированная матрица:")
for row in transposed_matrix:
    print(row)
