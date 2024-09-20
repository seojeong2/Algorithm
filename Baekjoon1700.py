n,k = map(int,input().split())
use = list(map(int,input().split()))

code = []
answer = 0

for i in range(k):
    if use[i] in code: # 이미 코드에 꽂혀있으면
        continue
    if len(code) < n: # 코드에 자리가 남으면
        code.append(use[i])
        continue

    priority = []
    for c in code:
        if c in use[i:]:
            priority.append(use[i:].index(c)) # 코드에 꽂혀있는 기기중에 다음번에 또 사용할게 있는지 체크
        else:
            priority.append(101) # 다시 사용하지 않는것은 101 값 넣음(범위가 100이 최대임)
    
    target = priority.index(max(priority)) # 값이 높은것 -> 우선순위가 낮은것
    code.remove(code[target])
    code.append(use[i])
    answer += 1
print(answer)