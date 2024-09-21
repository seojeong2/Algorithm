# 단어 배열이 있을때, 한줄에 문자를 K개 까지만 쓸수 있고, 단어와 단어 사이에는 '-'(구분자)가 있어야함

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(K, words):
	answer = 1
	wdLen = 0
	
	for i in range(len(words)):
		wdLen += len(words[i]) + 1
		
		if wdLen > K+1:
			answer += 1
			wdLen = len(words[i])+1
	return answer


K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

print("solution 함수의 반환 값은", ret, "입니다.")