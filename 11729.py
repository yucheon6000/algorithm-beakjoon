''' 
# 혼자 짜본 코드
# 실행은 되나 너무 많은 재귀로 인해서 중간에 끊김
import copy

board_size = 3

def move_tower(prev, to, state, total_size):
    if prev == to:
        return
    if len(state[prev]) <= 0:
        return
    if len(state[to]) > 0 and state[prev][0] > state[to][0]:
        return
    
    state = copy.deepcopy(state)

    target = state[prev][0]
    state[prev].pop(0)
    state[to].insert(0, target)

    print("state", prev, to, state)

    if len(state[board_size - 1]) == total_size:    # 마지막 칸이 꽉 차있으면
        print("result", state)
        return

    for _prev in range(board_size):
        for _to in range(board_size):
            if _prev == to and _to == prev:
                continue
            move_tower(_prev, _to, state, total_size)

k = int(input())

for x in range(board_size):
    state = [[int(x) for x in range(1, k + 1)],[],[]]
    move_tower(0, x, state, k)
'''

# 블로그 글의 원리를 보고 다시 생각해서 짜 봄
# 글을 읽어봤는데도 이해가 잘 안되어서 종이에 과정을 계속해서 적은 뒤에야 이해
# 너무 지엽적으로 들어가는 것보다
# 먼저 처리되어야 할 것이 무엇인지, 그 다음은.. 이렇게 러프하게 보는 것이 중요한 것 같다

'''
하노이 재귀함수
n       옮길 원판 개수
src     출발지
dest    목적지
aux     경유지
'''

def hanoi(n, src, dest, aux):   
    if n == 1:
        return print(src, dest)         # 출발지(src) -> 목적지(dest)
    
    else:
                                        # n개의 원판을 옮기려면
        hanoi(n - 1, src, aux, dest)    # n-1개의 원판을 경유지로 옮겨놓고
        hanoi(1, src, dest, aux)        # 1개의 원판을 목적지로 옮긴 후
        hanoi(n - 1, aux, dest, src)    # 경유지에 옮겨놨던 n-1개의 원판을 목적지로 옮기면 된다.

# 입력
k = int(input())

# 총 옮긴 횟수
def counter(n):
    if n == 1:
        return 0
    else:
        return counter(n - 1) + 2 ** (n - 1)

# print(counter(k) + 1)

print(2 ** k - 1) # 일반항

# 실행
hanoi(k, 1, 3, 2)
