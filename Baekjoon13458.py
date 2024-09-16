n = input()
data = list(map(int,input().split()))
b,c = map(int,input().split())

total = 0

for i in data:
    total += 1 # 총감독관

    if i > b:
        total += (i-b) // c

        if (i-b) % c != 0:
            total += 1 # 남은 학생들 부감독이 감시

print(total)