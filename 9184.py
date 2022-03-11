'''
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
'''

DATA = {}

# 해당 위치에 데이터를 저장하는 함수
def set_data(a, b, c, data):
    a_data = None
    if a in DATA:
        a_data = DATA[a]
    else:
        a_data = {}
        DATA[a] = a_data

    b_data = None
    if b in a_data:
        b_data = a_data[b]
    else:
        b_data = {}
        a_data[b] = b_data

    if c not in b_data:
        b_data[c] = data


# 해당 위치에 저장 데이터 존재 유무와 데이터 값을 반환하는 함수
def get_data(a, b, c):
    if a in DATA:
        a_data = DATA[a]
        if b in a_data:
            b_data = a_data[b]
            if c in b_data:
                return True, b_data[c]

    return False, None


# 문제 함수
def w(a, b, c):
    # 저장되어 있는 값이면 바로 반환
    flag, data = get_data(a, b, c)
    if flag:
        return data

    data = 0

    if a <= 0 or b <= 0 or c <= 0:
        data = 1
    elif a > 20 or b > 20 or c > 20:
        data = w(20, 20, 20)
    elif a < b < c:
        data = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        data = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    # 저장 후 반환
    set_data(a, b, c, data)
    return data


# 입력
while True:
    [a, b, c] = [int(x) for x in input().split()]
    
    # 종료
    if a == b == c == -1:
        break

    # 실행 및 출력
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
