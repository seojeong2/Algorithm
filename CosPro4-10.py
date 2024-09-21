# a이상 b 이하의 수중에 소수의 2제곱, 3제곱이 몇개있는지 계산하는 문제

def get_primes(n):
    primes = [2]
    for i in range(3,n+1,2):
        isPrime = True
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes

def solution(a,b):
    answer = 0
    primes = get_primes(b)

    # 2제곱 구하기
    for i in primes:
        now = pow(i,2)
        if a < now < b:
            answer += 1
    
    # 3제곱 구하기
    for i in primes:
        now = pow(i,3)
        if a < now < b:
            answer += 1
    
    return answer


a =  6
b =  30
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")