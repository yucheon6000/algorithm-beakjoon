import sys
import heapq

N = int(sys.stdin.readline().strip())
HEAP = []

for i in range(N):
    input_num = int(sys.stdin.readline().strip())
    heapq.heappush(HEAP, input_num)

for i in range(N):
    print(heapq.heappop(HEAP))
