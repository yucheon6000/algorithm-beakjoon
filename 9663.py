import sys

# 입력 및 변수 초기화
N = int(sys.stdin.readline().strip())
TOTAL_COUNT = 0
TABLE = [-1] * N

# 놓을 수 있는 자리인지 확인하는 함수
def placeable(cur_row, cur_col):
    for prev_row in range(cur_row):
        prev_col = TABLE[prev_row]
        # 같은 열에 놓을려고 하거나 대각선에 놓으려고 하는 경우
        if prev_col == cur_col or prev_col + prev_row == cur_col + cur_row or prev_col - prev_row == cur_col - cur_row:
            return False

    return True


# 퀸을 놓을 수 있는 경우의 수를 세는 함수
def n_queen(row_idx: int):
    global TOTAL_COUNT

    if row_idx == N:
        TOTAL_COUNT += 1
        return

    for col_idx in range(N):
        if placeable(row_idx, col_idx):
            TABLE[row_idx] = col_idx
            n_queen(row_idx + 1)


# 실행
n_queen(0)
print(TOTAL_COUNT)

# 파이썬으로 실행하면 시간초과가 남
# Pypy3으로 풀면 성공
