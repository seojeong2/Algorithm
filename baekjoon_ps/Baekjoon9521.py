a = input()
b = input()

lenA = len(a)
lenB = len(b)
lcs = [[0] * (lenB+1) for _ in range(lenA+1)]
for i in range(1,lenA+1):
    for j in range(1,lenB+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[lenA][lenB])
