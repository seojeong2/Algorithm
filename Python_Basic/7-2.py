# 재귀함수로 구현한 이진탐색 코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 칮은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array,target,mid+1,end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

# 이진탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않음")
else:
    print(result+1)


