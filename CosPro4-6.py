# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# k자리 수중 각 자리를 K제곱해서 더한 수가 본인이 되는 수 찾기

def power(base, exponent):
	val = 1
	for i in range(exponent):
		val *= base
	return val

def solution(k):
	answer = []
	bound = power(10, k)
	for i in range(bound // 10, bound):
		current = i
		calculated = 0
		while current != 0:
			calculated += power(current % 10, k)
			current //= 10
		if calculated == i:
			answer.append(i)
	return answer


k = 3
ret = solution(k)

print("solution 함수의 반환 값은", ret, "입니다.")
