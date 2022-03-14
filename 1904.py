'''
# 메모리 초과

import sys
sys.setrecursionlimit(10**6)

# 입력
N = int(input())

# 사용할 수 있는 단위
UNIT_LIST = ["1", "00"]

# 데이터 및 초기화
DATA = [[]] # 첫 칸은 인덱스 0 자리

for n in range(N):
    DATA.append([])

# 앞 뒤 어디에 놓을 지
DIR_LIST = [[1, 0], [0, 1]]

def f(seq):
    global DATA

    if len(seq) == N:
        return

    for unit in UNIT_LIST:
        for dir in DIR_LIST:
            new_seq = (seq * dir[0]) + unit + (seq * dir[1])  # 새로운 수열 생성 (앞 또는 뒤에 붙여서)
            length = len(new_seq)
            
            if length > N:  # 길이 초과 확인
                continue

            # 이미 있는 수열이면 중단
            # 없으면 계속 진행
            seq_list = DATA[length]
            if new_seq not in seq_list:
                seq_list.append(new_seq)
                f(new_seq)


f("")
print(int(len(DATA[N]) % 15746))
'''
# 입력
N = int(input())
DATA = [0] * (N + 1)

# 1 또는 2일 경우 출력 후 종료
if N == 1 or N == 2:
    print(N)
    exit()

# 초기화
DATA[1] = 1
DATA[2] = 2

# 실행
for i in range(3, N + 1):
    DATA[i] = (DATA[i-1] + DATA[i-2]) % 15746  # 마지막에 나눠주는 것이 아닌, 나눈 값을 저장해야 함 (너무 값이 커지는 것을 방지)

# 출력
print(DATA[N])
