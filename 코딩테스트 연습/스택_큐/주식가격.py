def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        isFallen = False
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                isFallen = True
                break
        if not isFallen:
            answer.append(len(prices) - 1 - i)
    answer.append(0)
    return answer

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]

    print(solution(prices))