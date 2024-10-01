n = int(input())


# 메모리 초과
# d = [0] * 1000001

# d[1] = 1
# d[2] = 2

# for i in range(3,n+1):
#     d[i] = d[i-1] + d[i-2]

# print(d[n] % 15746) 

arr = [0,1,2]
for i in range(3, n+1):
    arr.append(arr[i-1] + arr[i-2])

print(arr[n]%15746)