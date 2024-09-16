n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

result = 0
for i in range(len(data)-1,0,-1):
    if data[i] < data[i-1]:
        num = data[i-1] - data[i] + 1
        result += num
        data[i-1] -= num
    elif data[i] == data[i-1]:
        result += 1
        data[i-1] -= 1
    else:
        continue
print(result)