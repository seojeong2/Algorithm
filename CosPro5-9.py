from collections import deque
def solution(number, target):
    answer = 0

    if number >= target:
        return number - target
	
    max_limit = target * 2
    dp = [int(1e9)] * (max_limit + 1)
    dp[number] = 0

    q = deque([number])

    while q:
        curr = q.popleft()
        # 3가지 연산 수행
        next_pos = [curr-1, curr+1, curr*2]
        for pos in next_pos:
            if 0<=pos <= max_limit and dp[pos] > dp[curr] + 1:
                dp[pos] = dp[curr] + 1
                q.append(pos)
            if pos == target:
                return dp[target]
    return dp[target]


number1 = 5
target1 = 9
ret1 = solution(number1, target1)

print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

print("solution 함수의 반환 값은", ret2, "입니다.")