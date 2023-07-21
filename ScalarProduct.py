row = int(input())
col = int(input())
mat = [[int(input()) for x in range (col)] for y in range(row)]
mul = int(input())

for i in range(row):
    for j in range(col):
        mat[i][j] = mat[i][j] * mul

for i in range(row):
    for j in range(col):
        print(mat[i][j])
    print()

