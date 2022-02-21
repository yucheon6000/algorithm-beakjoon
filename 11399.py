person = int(input())
times = [int(x) for x in input().split()]

# 정렬 (버블소트)
i = person
while i > 0:
    j = 0
    while j < i - 1:
        if times[j] > times[j + 1]:
            temp = times[j]
            times[j] = times[j + 1]
            times[j + 1] = temp
        j += 1
    i -= 1

# 총 시간 계산
time_sum = 0
result = 0
for time in times:
    time_sum += time
    result += time_sum

print(result)