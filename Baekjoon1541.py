s = input()
s = s.split("-")

num = []
for i in s:
    total = 0
    tmp = i.split("+")
    for j in tmp:
        total += int(j)
    num.append(total)

result = num[0]
for i in range(1,len(num)):
    result -= num[i]

print(result)

