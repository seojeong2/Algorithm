n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input())))
b = []
for _ in range(n):
    b.append(list(map(int,input())))

result =  0

def reverse(i,j):
    for x in range(i,i+3):
        for y in range(j,j+3):
            if a[x][y] == 0:
                a[x][y] = 1
            else:
                a[x][y] = 0
for i in range(0,n-2):
    for j in range(0,m-2):
        if a[i][j] != b[i][j]:
            reverse(i,j)
            result += 1


isSame = True
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            isSame = False

if isSame:
    print(result)
else:
    print(-1)
    