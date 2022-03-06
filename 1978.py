import sys

N = int(sys.stdin.readline().strip())
NUM_LIST = [int(x) for x in sys.stdin.readline().strip().split()]
count = len(NUM_LIST)

for num in NUM_LIST:
    # 1은 소수 아님
    if num == 1:
        count -= 1
        continue
    
    # 2부터 num-1까지 순회하면서 나눠본다.
    # 나머지 없이 나뉘면 소수 아님
    for i in range(2, num):
        if num % i == 0:
            count -= 1
            break

print(count)
