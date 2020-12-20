file = open("matrix.txt","r")
data = file.readlines()
file.close()
matrix =[]

for line in data:
    mat_list = line.split(' ')
    matrix.append(mat_list)
col_itr = 0
max_num = 0
max_col = col_itr + 1

for col in matrix[0]:
    sum_col = 0
    row_itr = 0
    for row in matrix:
        sum_col += int(matrix[row_itr][col_itr])
        row_itr += 1
    print(sum_col, 'Сумма чисел в столбце', col_itr + 1)
    col_itr += 1
    if max_num < sum_col:
        max_num = sum_col
        max_col = col_itr
print(max_num, '- Максимальная сумма в ', max_col, " строке")

