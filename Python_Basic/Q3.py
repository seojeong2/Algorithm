count0 = 0 # 전부 0으로 바꾸는 횟수
count1 = 0 # 전부 1로 바꾸는 횟수

data = input()

if data[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
    print('count0: ', count0, 'count1', count1)

print(min(count0, count1))

