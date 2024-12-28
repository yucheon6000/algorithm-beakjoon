import sys

# 입력 및 변수 초기화
N = int(sys.stdin.readline().strip())
TOTAL_COUNT = 0
TABLE = []

# 퀸 위치를 기준으로 가로, 세로, 대각선의 불리언을 바꿔주는 함수
def placeable(row_idx: int, col_idx: int):
    # 가로
    row = TABLE[row_idx]
    for i in range(N):
        val = row[i]
        if val == 0:
            return False
    
    # 세로
    for r in range(N):
        val = TABLE[r][col_idx]
        if val == 0:
            return False
    
    # 대각선
    dir_list = [[1, 1], [1, -1], [-1, 1], [-1, -1]]  # [[r_dir, c_dir], ...]
    for dir in dir_list:
        r_i = row_idx
        c_i = col_idx
        while 0 <= r_i < N and 0 <= c_i < N:
            val = TABLE[r_i][c_i]
            if val == 0:
                return False
            r_i += dir[0]
            c_i += dir[1]

    return True

A = False
def n_queen(cnt: int):
    global TOTAL_COUNT, A

    if cnt == N:
        TOTAL_COUNT += 1
        A = True
        return
    
    for i in range(N):
        for j in range(N):
            if TABLE[i][j] == 0 or not placeable(i, j):
                continue
            
            TABLE[i][j] = 0
            if not A:
                print(cnt, i, j)
                print('\n'.join(''.join(map(str, i)) for i in TABLE))
                print("-------")
            n_queen(cnt + 1)
            TABLE[i][j] = 1
            if not A:
                print(cnt, i, j)
                print('\n'.join(''.join(map(str, i)) for i in TABLE))
                print("-------")

    return


# 테이블 초기화
for i in range(N):
    row = []
    for j in range(N):
        row.append(1)
    TABLE.append(row)

# 실행
n_queen(0)
print(TOTAL_COUNT)