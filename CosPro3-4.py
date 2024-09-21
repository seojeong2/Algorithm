def solution(s1, s2):
	answer = 0
	
	# 첫번째 문자열(s1)만큼 반복
	for i in range(len(s1)):
		if s1[0:i] == s2[-i:]:
			answer = i
			break
	
	# 두번째 문자열(s2)만큼 반복
	for i in range(len(s2)):
		if s2[0:i] == s1[-i:]:
			if answer < i:
				answer = i
				break
				
	answer = len(s1) + len(s2) - answer
	return answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)

print("solution 함수의 반환 값은", ret, "입니다.")