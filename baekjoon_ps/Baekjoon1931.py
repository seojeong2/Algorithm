n  = int(input())

times = []
for _ in range(n):
    start, end = map(int,input().split())
    times.append([start,end])


# 회의를 끝나는 시간 기준으로 정렬 -> 회의가 빨리끝나야 다음 회의를 진행가능
times.sort(key=lambda x:(x[1],x[0]))

result = 0
end_t = 0

for i in times:
    if end_t <= i[0]:
        result += 1
        end_t = i[1]

print(result)