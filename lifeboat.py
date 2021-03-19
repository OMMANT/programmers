# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people = sorted(people)
    c_limit = limit
    rescued = 0
    while len(people) > 0:
        if rescued >= 2:
            c_limit = limit
            rescued = 0
            answer += 1
        if c_limit >= people[0]:
            c_limit -= people.pop(0)
            rescued += 1
        else:
            c_limit = limit
            rescued = 0
            answer += 1
    answer += 1
    return answer


if __name__ == '__main__':
    peoples = [
        [70, 50, 80, 50],
        [70, 80, 50],
        [40, 50, 240, 60, 70, 80, 90, 100]
    ]
    limits = [
        100,
        100,
        240,
    ]
    answers = []

    for people, limit in zip(peoples, limits):
        answers.append(solution(people, limit))
    print(answers)