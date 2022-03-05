import sys
from typing import List

'''
[END_NUM, MAX_COUNT] = [int(x) for x in sys.stdin.readline().strip().split()]

# 수열 만드는 함수
def make_sequence(list: List, num: int):
    if num in list:
        return
        
    list.append(num)

    if len(list) == MAX_COUNT:
        print(' '.join(map(str, list)))

    else:
        for i in range(1, END_NUM + 1):
            make_sequence(list.copy(), i)


# 실행
for i in range(1, END_NUM + 1):
    make_sequence([], i)
'''

[END_NUM, MAX_COUNT] = [int(x) for x in sys.stdin.readline().strip().split()]

# 수열 만드는 함수
def make_sequence(list: List):
    if len(list) == MAX_COUNT:
        print(' '.join(map(str, list)))
        return
    
    for i in range(1, END_NUM + 1):
        if i in list:
            continue
        list.append(i)
        make_sequence(list)
        list.pop()

make_sequence([])