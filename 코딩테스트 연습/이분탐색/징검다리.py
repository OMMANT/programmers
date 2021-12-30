def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    l, r = 0, distance
    while l <= r:
        m = (l + r) // 2
        min_d = distance
        removed = 0
        position = 0

        for rock in rocks:
            d = rock - position
            if d < m:
                removed += 1
            else:
                position = rock
                min_d = min(min_d, d)
        
        if removed > n:
            r = m - 1
        else:
            answer = min_d
            l = m + 1
    return answer


if __name__ == '__main__':
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n))