import sys

n = int(sys.stdin.readline().strip())
target = '666'
current_n = 0
i = 665
while True:
    i += 1
    i_str = str(i)
    if i_str.find(target) >= 0:
        current_n += 1
        if current_n == n:
            print(i)
            break
