import sys

input_val_list = []

# 입력
n = int(sys.stdin.readline().strip())
for i in range(n):
    input_val = int(sys.stdin.readline().strip())
    input_val_list.append(input_val)

# 정렬
input_len = len(input_val_list)
for i in range(input_len - 1):
    for j in range(input_len - 1 - i):
        a = input_val_list[j]
        b = input_val_list[j + 1]
        if a > b:
            input_val_list[j] = b
            input_val_list[j + 1] = a

for val in input_val_list:
    print(val)
