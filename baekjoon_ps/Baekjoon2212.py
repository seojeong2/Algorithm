n = int(input())
k = int(input())

sensor = list(map(int,input().split()))
sensor.sort()

distance = []
for i in range(1,n):
    distance.append(sensor[i] - sensor[i-1])

distance.sort(reverse=True)

print(sum(distance[k-1:]))
