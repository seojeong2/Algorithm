k = int(input())

d = [[0,0]]

d.append([0,1])
d.append([1,1])

for i in range(3,k+1):
    d.append([d[i-1][0] + d[i-2][0], d[i-1][1]+d[i-2][1]])

print(d[k][0], d[k][1])
#print(d)

