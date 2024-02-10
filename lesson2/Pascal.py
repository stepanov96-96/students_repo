n = int(input("Введите число: "))
p = []

for i in range(n):
    row = [1] * (i+1)
    for j in range(1, i):
        if j !=0 and j !=i:
            row[j] = (p[i-1][j-1]+p[i-1][j])

    p.append(row)

for r in p:
    print(r)