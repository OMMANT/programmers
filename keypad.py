# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

def solution(numbers, hand):
    answer = ''

    current_left_pos = (0, 0)
    current_right_pos = (2, 0)

    for idx, num in enumerate(numbers):
        print(f'[{idx}]\ncurrent_left_pos: {current_left_pos}\ncurrent_right_pos: {current_right_pos}')
        print(f'number: {num}')
        if num in [1, 4, 7]:
            answer += 'L'
            current_left_pos = (0, (10 - num) // 3)
        elif num in [3, 6, 9]:
            answer += 'R'
            current_right_pos = (2, (12 - num) // 3)
        elif num in [2, 5, 8, 0]:
            num_pos = (1, (11 - num) // 3 if num != 0 else 0)
            l_dist = sum([abs(x2 - x1) for x1, x2 in zip(num_pos, current_left_pos)])
            r_dist = sum([abs(x2 - x1) for x1, x2 in zip(num_pos, current_right_pos)])
            print(f'num_pos:{num_pos}\n(l_dist, r_dist): {(l_dist, r_dist)}')
            if l_dist < r_dist:
                answer += 'L'
                current_left_pos = num_pos
            elif l_dist > r_dist:
                answer += 'R'
                current_right_pos = num_pos
            elif hand == 'left':
                answer += 'L'
                current_left_pos = num_pos
            else:
                answer += 'R'
                current_right_pos = num_pos
        print(f'answer:{answer}', '\n')

    return answer


if __name__ == '__main__':
    numbers_lst = [
        [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
        [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
        [0, 1, 0, 7, 1, 2, 8, 4, 7, 9, 5, 0],
    ]
    hand_lst = [
        'right',
        'left',
        'right',
        'left',
    ]

    result_lst = []

    for numbers, hand in zip(numbers_lst, hand_lst):
        result_lst.append(solution(numbers, hand))

    print(result_lst)
