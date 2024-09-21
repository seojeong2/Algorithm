def solution(bishops):
	answer = 0
	
	dxdy = [[1,1],[1,-1],[-1,-1],[-1,1]]
	arr = [[0 for _ in range(8)] for _ in range(8)]
	
	for i in bishops:
		x = 8 - int(i[1]) # 행
		y = ord(i[0]) - 65
		
		arr[x][y] = 1
		
		for dx,dy in dxdy:
			nx,ny = x,y
			while True:
				nx += dx
				ny += dy
				
				if 0 > nx or nx >= 8 or 0 > ny or ny >= 8: break
				
				arr[nx][ny] = 1
		
	cnt = 0
	for i in range(8):
		for j in range(8):
			if arr[i][j] == 1:
				cnt += 1
	answer = 64 - cnt
	return answer


bishops1 = ["D5"]
ret1 = solution(bishops1)

print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

print("solution 함수의 반환 값은", ret2, "입니다.")