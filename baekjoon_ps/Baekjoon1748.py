n = int(input())

n_len = len(str(n))

# 나머지
result = 0

result += ((n - 10 ** (n_len -1)) + 1) * n_len

for i in range(n_len-1): 
    result += 9 * (10**i) * (i+1)
    i += 1
print(result)