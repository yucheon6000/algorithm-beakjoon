# 정렬 (버블소트)
def sort(arr):
    result = arr.copy()
    length = len(result)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if result[j] > result[j + 1]:
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
    
    return result


# 검색 (이분탐색)
def search(sorted_arr, target):
    length = len(sorted_arr)

    start_index = 0
    end_index = length - 1

    while True:
        center_idx = int((start_index + end_index) / 2)
        center = sorted_arr[center_idx]
        
        if center == target:
            return True
        elif start_index == end_index:
            return False
        elif center > target:
            end_index = center_idx - 1
        else:
            start_index = center_idx + 1

        if start_index > end_index:
            break

    return False
    

# 입력
n = int(input())
arr = [int(x) for x in input().split()]
# arr = sort(arr)  # 버블소트로 정렬하면 시간초과 나옴
arr.sort()

# 실행
m = int(input())
target_list = [int(x) for x in input().split()]
for target in target_list:
    if search(arr, target):
        print(1)
    else:
        print(0)
