'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
'''

import sys

FIBONACCI_DATA = [None] * 50

FIBONACCI_DATA[0] = [1, 0]
FIBONACCI_DATA[1] = [0, 1]

# 피보나치 0, 1 출력 횟수 계산하는 함수
def fibonacci(n):
    global FIBONACCI_DATA

    # 미리 계산한 피보나치 수가 없을 경우 
    if FIBONACCI_DATA[n] is None:
        prev_fibo = fibonacci(n - 1)
        prev_prev_fibo = fibonacci(n - 2)

        zero_cnt = prev_fibo[0] + prev_prev_fibo[0]
        one_cnt  = prev_fibo[1] + prev_prev_fibo[1]
        result = [zero_cnt, one_cnt]
        
        FIBONACCI_DATA[n] = result
        return result

    else:
        return FIBONACCI_DATA[n]


# 입력
N = int(sys.stdin.readline().strip())

# 실행 및 출력
for i in range(N):
    num = int(sys.stdin.readline().strip())
    [zero_cnt, one_cnt] = fibonacci(num)
    print(zero_cnt, one_cnt)
