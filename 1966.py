case_count = int(input())

for case in range(case_count):
    # 입력
    [paper_count, target_index] = [int(x) for x in input().split()]  # [큐 길이, 목표 요소의 위치]
    queue = [int(x) for x in input().split()]

    current_target_index = target_index  # 목표 요소의 현재 인덱스 위치
    pop_count = 0  # 꺼낸 횟수

    while True:
        # 첫번째 요소 꺼내기
        first = queue.pop(0)
        
        # 뒤에 높은 우선순위 있나 확인
        flag = False
        for i in queue:
            if first < i:
                flag = True
                break

        # 뒤에 높은 우선순위가 있으면, 첫번째 요소 맨 뒤에 넣기
        if flag:
            queue.append(first)

            if current_target_index == 0:
                current_target_index = len(queue) - 1
            else:
                current_target_index -= 1
        
        # 뒤에 높은 우선순위가 없으면, 첫번쨰 요소 버리기
        else:
            pop_count += 1  # 꺼냄 +1

            if current_target_index == 0:
                print(pop_count)
                break
            else:
                current_target_index -= 1
