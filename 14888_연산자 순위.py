num_list = [1, 2, 3, 4, 5, 6]
sign_list = ["-", "/", "+", "+", "*"]

stack = []

def calc():
    for i in range(len(num_list) + len(sign_list)):
        idx = i // 2
        
        # 숫자 차례
        if i % 2 == 0:
            cur_num = num_list[idx]

            # 첫 숫자는 그냥 삽입만 함
            if i == 0:
                stack.append(cur_num)
                continue

            # 직전의 연산자를 꺼내고
            sign = stack.pop()
        
            # 곱하기나 나누기면 먼저 계산 후, 결과 삽입
            if sign == "*" or sign == "/":
                prev_num = stack.pop()
                result = (prev_num * cur_num) if sign == "*" else (prev_num // cur_num)
                stack.append(result)
            
            # 더하기나 빼기면 꺼낸 연산자와 숫자 그대로 삽입
            else:
                stack.append(sign)
                stack.append(cur_num)

        # 연산자 차례
        else:
            sign = sign_list[idx]
            stack.append(sign)

    result = 0
    print(stack)
    if len(stack) == 1:
        result = stack[0]
        return result

    for i in range(len(stack)):
        # 숫자 차례
        if i % 2 == 0:
            cur_num = stack[i]

            if i == 0:
                result += cur_num
                continue

            sign = stack[i-1]
            result = result + cur_num if sign == "+" else result - cur_num
    
    return result
            

print(calc())
