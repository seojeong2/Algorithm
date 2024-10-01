n = int(input())
flowers = [list(map(int,input().split())) for _ in range(n)]
flowers.sort()

i = 0
result = 0
latest_end = (3,1)

while i < n:
    sm, sd, em, ed = flowers[i]
    if (sm,sd) <= latest_end < (em,ed):
        max_end = (em,ed)

        while i < n - 1: # 현재 심을 수 있는 꽃들 중에서 가장 마지막에 지는 꽃 찾기 시작
            nsm, nsd, nem, ned = flowers[i+1]
            if latest_end < (nsm, nsd): # 현재 심을 수 있는 꽃이 i번째 까지라면 종료
                break
            if max_end < (nem,ned):
                max_end = (nem,ned)
            i+=1
        result += 1
        latest_end = max_end

        if (11,30) < latest_end:
            print(result)
            exit(0)
    i+=1
print(0)