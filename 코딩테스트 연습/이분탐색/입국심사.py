def solution(n, times):
    n_examiner = len(times)
    times.sort()
    min_time, max_time = times[0], times[-1]
    left, right = min_time, max_time * n
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        examined = 0
        for time in times:
            examined += mid // time
            if examined >= n:
                break
        if examined >= n:
            answer = mid
            right = mid - 1
        elif examined < n:
            left = mid + 1
    return answer

if __name__ == '__main__':
    n = 6
    times = [7, 10]
    test = times[:]
    test[0] *= 2
    print(times, test)
    sol = solution(n, times)
    print(sol)