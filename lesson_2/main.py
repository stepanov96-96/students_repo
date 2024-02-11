N = 7
P = []

for i in range(N):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = P[i - 1][j - 1] + P[i - 1][j]

    P.append(row)

for r in P:
    print(r)
