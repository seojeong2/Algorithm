import sys
 
n = int(input())
array = list(map(int,input().split())) # 매장에 있는 부품

m = int(input())
x = list(map(int,input().split())) # 손님이 요구한 리스트


def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in x:
    result = binary_search(array, i, 0,n-1)
    if result != None:
        print('yes', end= ' ')
    else:
        print('no', end=' ')