n = int(input())
text = input().rstrip()
ans = 0
for i in range(n):
    ans += (ord(text[i]) - 96) * (31 ** i)

print(ans)