# 입력
[N, M] = [int(x) for x in input().split()]

SEQ = [] # 수열

def f():
    global SEQ

    len_seq = len(SEQ)

    # 길이가 충족되면 출력
    if len_seq == M:
        print(' '.join(map(str, SEQ)))

    # 1 ~ N 범위의 수
    for i in range(1, N+1):
        if len_seq == 0 or SEQ[-1] < i:
            SEQ.append(i)
            f()
            SEQ.pop()


# 실행
f()
