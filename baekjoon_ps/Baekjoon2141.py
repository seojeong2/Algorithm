n = int(input())
people = 0
village = []

for i in range(n):
    pos,peo = map(int,input().split())
    people += peo
    village.append((pos,peo))

village.sort()

cnt = 0
for pos, peo in village:
    cnt += peo
    if cnt >= people / 2:
        print(pos)
        break

    