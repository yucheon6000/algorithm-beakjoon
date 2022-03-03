'''
# 힙을 구현했는데 틀림
import sys
from typing import List

def heapify(heap: List, input: int):
    heap.append(input)
    heap_len = len(heap)
    cur_idx = heap_len - 1

    while cur_idx > 0:
        root_idx = cur_idx // 2 if cur_idx % 2 == 0 else (cur_idx - 1) // 2
        
        # 부모값과 현재값
        root = heap[root_idx]
        cur = heap[cur_idx]

        root_abs = abs(root)
        cur_abs = abs(cur)

        # (현재값의 절대값이 작을 때) or (현재값의 절대값과 부모값의 절대값이 같은데 현재값이 더 작을 때)
        if (cur_abs < root_abs) or (cur_abs == root_abs and cur < root):
            heap[cur_idx] = root
            heap[root_idx] = cur
            cur_idx = root_idx
        else:
            break    


def pop_from_heap(heap: List) -> int:
    # 길이 0일 때 예외처리
    heap_len = len(heap)
    if heap_len == 0:
        return 0

    # 첫번째 값 꺼내고, 마지막 값을 맨 앞에 둠
    pop_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    heap_len -= 1

    cur_idx = 0
    l_idx = cur_idx * 2 + 1
    while l_idx < heap_len:
        r_idx = l_idx + 1

        # 부모값(현재값)과 자식값
        cur = heap[cur_idx]
        l = heap[l_idx]
        r = heap[r_idx] if r_idx < heap_len else 0

        cur_abs = abs(cur)
        l_abs = abs(l)
        r_abs = abs(r)

        if cur_abs <= l_abs and cur_abs <= r_abs and cur <= l and cur <= r:
            break
        # (현재값의 절대값이 자식값의 절대값보다 크거나 두 절대값은 같은데 실제값이 더 크고) and (r이 0이거나 형제보다 작을 때)
        elif (r == 0) or (((cur_abs > l_abs) or (cur_abs == l_abs and cur > l)) and (r_abs >= l_abs)):
            heap[cur_idx] = l
            heap[l_idx] = cur
            cur_idx = l_idx
        elif (r != 0) and (((cur_abs > r_abs) or (cur_abs == r_abs and cur > r)) and (l_abs >= r_abs)):
            heap[cur_idx] = r
            heap[r_idx] = cur
            cur_idx = r_idx
        else:
            break

        l_idx = cur_idx * 2 + 1

    return pop_val


# 입력 및 실행
n = int(sys.stdin.readline().strip())
heap = []

for i in range(n):
    input_val = int(sys.stdin.readline().strip())

    if input_val != 0:
        heapify(heap, input_val)
    else:
        print(pop_from_heap(heap))
'''

'''새 풀이'''
import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []

for i in range(n):
    input_val = int(sys.stdin.readline().strip())
    
    if input_val == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(input_val), input_val))
