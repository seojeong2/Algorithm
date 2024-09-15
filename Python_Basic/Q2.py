s = input()

total = int(s[0])
for i in range(1,len(s)):
    if total <= 0: 
        total += int(s[i])
    else:
        total *= int(s[i])

print(total)
