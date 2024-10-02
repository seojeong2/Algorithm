str1 = input()
str2 = input()

i = 0
cnt = 0

while i < len(str1):
    if str1[i:i+len(str2)] == str2:
        i += len(str2)
        cnt += 1
    else:
        i += 1

print(cnt)