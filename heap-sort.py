def heapify(arr, n, i):
    largest = i  # 루트를 가장 큰 값으로 가정
    left = 2 * i + 1  # 왼쪽 자식 노드
    right = 2 * i + 2  # 오른쪽 자식 노드

    # 왼쪽 자식이 루트보다 큰 경우
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식이 가장 큰 경우 갱신
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 가장 큰 값이 루트가 아니면 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # 재귀적으로 힙 구조를 유지
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 배열을 최대 힙으로 변환
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 추출하여 정렬
    for i in range(n - 1, 0, -1):
        # 루트(가장 큰 값)와 마지막 요소를 교환
        arr[i], arr[0] = arr[0], arr[i]
        
        # 교환된 부분을 제외하고 힙 구조 유지
        heapify(arr, i, 0)

# 예시 실행
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)
