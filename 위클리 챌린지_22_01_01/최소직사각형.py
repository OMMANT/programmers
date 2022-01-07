def solution(sizes):
    width = []
    height = []
    for size in sizes:
        width.append(max(size))
        height.append(min(size))
    answer = max(width) * max(height)
    return answer

if __name__ == '__main__':
    sizeses = [
        [[60, 50], [30, 70], [60, 30], [80, 40]],
        [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
        [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	
    ]

    for sizes in sizeses:
        print(solution(sizes))