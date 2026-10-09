mat = []
with open ('matrix.txt', 'r') as f:
    for line in f:
        stroki = [int(x) for x in line.split()]
        mat.append(stroki)
for k in range(8):
    col_k = [mat[i][k] for i in range(8)]
    if mat[k] == col_k:
        print(f"Строка {k} равна столбцу {k}")
            