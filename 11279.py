import sys
from typing import List

# 힙에 수를 넣는 함수
def append_to_heap(heap: List, input_value: int):
    current_index = len(heap)
    heap.append(input_value)

    while current_index > 0:
        # 부모 인덱스 초기화
        root_index = 0

        if current_index % 2 == 0:  # 본인이 우측 자식일 경우
            root_index = (current_index - 1) // 2
        else:
            root_index = current_index // 2

        # 부모 및 형제 수 획득
        root  = heap[root_index]
        current = heap[current_index]

        # 부모와 값 비교 후, 크면 스왑
        if current > root:
            heap[root_index] = current
            heap[current_index] = root
        else:
            break

        # 현재 인덱스 부모로 이동
        current_index = root_index

    return heap


# 힙에서 최대값(0번 값)을 뽑는 함수
def pop_from_heap(heap: List):
    heap_length = len(heap)
    if heap_length == 0:
        return 0

    # 맨 앞의 숫자는 없애고, 마지막 수를 뽑아서 맨 앞에 둠
    pop_value = heap[0]
    heap[0] = heap[-1]
    heap[-1] = pop_value
    heap.pop()
    heap_length -= 1

    # heapify Top-Down
    current_index = 0
    left_index = current_index * 2 + 1
    while left_index < heap_length:  # 왼쪽 자식이 있을 경우
        root = heap[current_index]
        left = heap[left_index]
        right = -1

        right_index = left_index + 1
        if right_index < heap_length:
            right = heap[right_index]

        if root >= left and root >= right:
            break
        elif left > right:
            heap[left_index] = root
            heap[current_index] = left
            current_index = left_index
        else:
            heap[right_index] = root
            heap[current_index] = right
            current_index = right_index

        # 왼쪽 자식 인덱스 계산
        left_index = current_index * 2 + 1

    return pop_value


# 변수 초기화
heap = []

# 입력
n = int(sys.stdin.readline())  # input() 함수 쓰면 시간초과 남
for i in range(n):
    input_value = int(sys.stdin.readline())
    if input_value == 0:
        result = pop_from_heap(heap)
        print(result)
    else:
        append_to_heap(heap, input_value)
