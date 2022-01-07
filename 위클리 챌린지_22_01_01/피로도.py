from itertools import permutations

def solution(k, dungeons):
    answers = []
    for p in permutations(dungeons, len(dungeons)):
        fatigue = k
        n = 0
        for dungeon in p:
            if fatigue > 0 and fatigue >= dungeon[0]:
                n += 1
                fatigue -= dungeon[1]
            else:
                break
        answers.append(n)
    return max(answers)

if __name__ == '__main__':
    k = 80
    dungeons = [
        [80, 20], [50, 40], [30, 10]
    ]
    print(solution(k, dungeons))