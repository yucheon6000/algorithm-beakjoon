# 괄호 문자열 유효 체크
def check_vps(ps_string):
    ps_list = list(ps_string)

    '''
    # 변수 사용
    left_cnt = 0
    for p in ps_list:
        if p == "(":
            left_cnt += 1
        else:
            left_cnt -= 1

        if left_cnt < 0:
            return False            

    if left_cnt == 0:
        return True
    else:
        return False
    '''

    # 스택 사용
    stack = []
    for p in ps_list:
        if p == "(":
            stack.append("(")
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


# 실행
n = int(input())
for i in range(n):
    ps_string = input()
    if(check_vps(ps_string)):
        print("YES")
    else:
        print("NO")
