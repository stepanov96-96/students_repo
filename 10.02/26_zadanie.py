b = [[1]]
n = 7
for i in range(1, n):
    row = [1]
    for j in range(1, i):
        row.append(b[i - 1][j - 1] + b[i - 1][j])
    row.append(1)
    b.append(row)
for row in b:
    print(*row)