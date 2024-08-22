n,x = map(int,input().split())
arr = list(map(int, input().split()))

if max(arr) == 0:
    print("SAD")
    exit(0)

val = sum(arr[:x])
max_val = val
cnt = 1

for i in range(x,n):
    val += arr[i]
    val -= arr[i-x]

    if val > max_val:
        max_val = val
        cnt = 1
    elif val == max_val:
        cnt += 1

print(max_val)
print(cnt)


