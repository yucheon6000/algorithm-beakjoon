import sys

# 연산자의 우선순위 없는 사칙연산 결과를 반환하는 함수
def calc(num_list, sign_list):
    result = 0
    for i in range(len(num_list)):
        cur_num = num_list[i]

        # 첫 숫자는 그냥 삽입만 함
        if i == 0:
            result += cur_num
            continue
        
        # 연산자 확인
        sign_idx = i - 1
        sign = sign_list[sign_idx]

        # 연산
        if sign == 0:
            result += cur_num
        elif sign == 1:
            result -= cur_num
        elif sign == 2:
            result *= cur_num
        elif sign == 3:
            if result < 0:
                result = -(-result // cur_num)
            else:
                result //= cur_num

    return result
            

# 입력
N = int(sys.stdin.readline().strip())
NUM_LIST = [int(x) for x in sys.stdin.readline().strip().split()]
SIGN_COUNT_LIST = [int(x) for x in sys.stdin.readline().strip().split()]

# 연산자를 넣을 리스트
SIGN_SEQ = [-1] * (N-1)

# 결과 변수 초기화
MAX_NUM = -1000000001
MIN_NUM = 1000000001


# 최댓값, 최솟값 계산하는 함수
def find_max_num_and_min_num(idx):
    global SIGN_COUNT_LIST, MAX_NUM, MIN_NUM

    # 연산자 개수가 모두 찰 경우
    if idx == N - 1:
        result = calc(NUM_LIST, SIGN_SEQ)
        if result < MIN_NUM:
            MIN_NUM = result
        if result > MAX_NUM:
            MAX_NUM = result
        return

    # 연산자가 남아있을 경우 연산을 해봄
    # 4는 사칙연산을 의미하는 숫자
    for sign_idx in range(4):
        sign_left_count = SIGN_COUNT_LIST[sign_idx]
        if sign_left_count > 0:
            SIGN_COUNT_LIST[sign_idx] -= 1
            SIGN_SEQ[idx] = sign_idx
            find_max_num_and_min_num(idx + 1)
            SIGN_COUNT_LIST[sign_idx] += 1
            SIGN_SEQ[idx] = -1
    

# 실행 및 결과 출력
find_max_num_and_min_num(0)
print(MAX_NUM)
print(MIN_NUM)
