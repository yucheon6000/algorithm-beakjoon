# 색 변경 함수
def flip_color(color):
    if color == "B":
        return "W"
    else:
        return "B"


# 색 변경 함수 (리스트)
def flip_color_list(color_list):
    result = []
    for color in color_list:
        result.append(flip_color(color))

    return result


# 보드 검증 함수
def get_change_count(start_index, current_min_count):
    [start_index_col, start_index_row] = start_index

    # 첫번째는 시작색 기준으로, 두번째는 시작색의 반대 기준으로
    start_color = "W"
    next_color_list = ["B", "W"]
    
    count_list = [0, 1]  # 두번째는 시작색과 반대로 시작하니까 1로 시작

    i = 0
    while i < target_size_col:
        col_index = start_index_col + i
        
        j = 0
        while j < target_size_row:
            row_index = start_index_row + j
            current_color = input_board[col_index][row_index]

            # 첫 번째 색이 초기값과 다를 때 초기화
            if i == 0 and j == 0:
                if current_color != start_color:
                    start_color = flip_color(start_color)
                    next_color_list = flip_color_list(next_color_list)

            else:
                # 다음색과 현재색 비교 후 카운트 변경
                c = 0
                while c < len(next_color_list):
                    if current_color != next_color_list[c]:
                        count_list[c] += 1
                    c += 1
                
                # 본 함수에서 구해지는 모든 카운트들이 매개변수로 받은 카운트 값보다 커지면 함수 종료
                if min(count_list) >= current_min_count:
                    return current_min_count

                # 다음색 변경
                next_color_list = flip_color_list(next_color_list)

            j += 1
        
        # 가로가 짝수면 다음색을 한 번 바꿈
        if target_size_row % 2 == 0:
            next_color_list = flip_color_list(next_color_list)

        i += 1

    return min(count_list)


# 시작
input_size = [ int(x) for x in input().split() ]
[input_size_col, input_size_row] = input_size

# 보드 생성
input_board = []
i = 0
while i < input_size_col:
    row = list(input())
    input_board.append(row)
    i += 1

target_size_col = target_size_row = 8

# 보드 검증
min_count = target_size_col * target_size_row  # 모든 보드를 다 바꿀 때의 수

i = 0
while i <= input_size_col - target_size_col:
    j = 0
    count = 0
    while j <= input_size_row - target_size_row:
        start_index = [i, j]
        change_count = get_change_count(start_index, min_count)
        if change_count < min_count:
            min_count = change_count

        j += 1

    i += 1

print(min_count)
