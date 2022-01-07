from itertools import combinations
from operator import itemgetter

def solution(line):
    answer = []
    meets = []
    for l1, l2 in combinations(line, 2):
        A, B, E = l1
        C, D, F = l2
        discriminant = A*D - B*C
        if discriminant != 0:
            x, y = (B*F - E*D) / discriminant, (E*C - A*F) / discriminant
            if x % 1 == 0 and y % 1 == 0:                
                x, y = map(int, (x, y))
                meets.append((x, y))
    meets = set(meets)
    min_x, max_x = min(map(itemgetter(0), meets)), max(map(itemgetter(0), meets))
    min_y, max_y = min(map(itemgetter(1), meets)), max(map(itemgetter(1), meets))
    
    for y in range(max_y, min_y-1, -1):
        s = ''
        for x in range(min_x, max_x+1):
            if (x, y) in meets: s += '*'
            else: s += '.'
        answer.append(s)
    return answer

if __name__ == '__main__':
    lines = [
        [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]],
        [[0, 1, -1], [1, 0, -1], [1, 0, 1]],
        [[1, -1, 0], [2, -1, 0]],
        [[1, -1, 0], [2, -1, 0], [4, -1, 0]],
    ]

    for line in lines:
        print(solution(line))