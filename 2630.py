# 변수 초기화
input_paper = []        # 입력받은 종이
paper_count = [0, 0]    # 각 색종이의 개수

# 같은 색깔인지 확인하는 함수
def check_same_color(start_index, length):
    [col, row] = start_index
    start_color = input_paper[col][row]

    for i in range(length):
        for j in range(length):
            cur_color = input_paper[col + i][row + j]
            if cur_color != start_color:
                return False, start_color

    return True, start_color


# 종이 확인 후, 개수 세는 함수 (재귀)
def check_paper(index, length):
    flag, color = check_same_color(index, length)

    if flag:
        paper_count[color] += 1
        return
    else:
        new_length = int(length / 2)
        for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:  # 4분할하여 다시 확인
            new_index = [index[0] + (i[0] * new_length), index[1] + (i[1] * new_length)]  # 기존 인덱스에 새 길이만큼을 더해준 새 인덱스 생성
            check_paper(new_index, new_length)


# 입력
n = int(input())
for i in range(n):
    input_paper.append([int(x) for x in input().split()])

# 실행
check_paper([0, 0], n)

# 출력
print(paper_count[0])
print(paper_count[1])