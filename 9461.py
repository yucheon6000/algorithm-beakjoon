import sys

# 입력
N = int(sys.stdin.readline().strip())

# 데이터 초기화
DATA = [-1] * 200
DATA[0] = 0
DATA[1] = 1
DATA[2] = 1
DATA[3] = 1
DATA[4] = 2
DATA[5] = 2

for i in range(N):
    T = int(sys.stdin.readline().strip())
    for j in range(1, T + 1):
        # 이미 저장되어 있을 경우, 건너뜀
        if DATA[j] != -1:
            continue
        
        # 데이터 저장
        DATA[j] = DATA[j-1] + DATA[j-5]

    # 출력
    print(DATA[T])
