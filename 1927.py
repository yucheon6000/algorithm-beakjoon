import sys
import heapq

n = int(sys.stdin.readline().strip())
heap = []

for i in range(n):
    input_value = int(sys.stdin.readline().strip())
    if input_value == 0:
        if heap:
            print(heapq.heappop(heap))  # 힙에서 최소값(0 인덱스 값) 삭제 및 출력
        else:
            print(0)

    else:
        heapq.heappush(heap, input_value)  # 힙에 요소 추가
