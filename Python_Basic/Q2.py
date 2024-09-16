s = input()

total = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])

    if num <=1 or total <= 1:
        total += num
    else:
        total *= num

print(total)
