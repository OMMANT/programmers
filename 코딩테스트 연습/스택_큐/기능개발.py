from math import ceil

def solution(progresses, speeds):
    takes = []
    answer = []

    for progress, speed in zip(progresses, speeds):
        takes.append(ceil((100 - progress) / speed))
    i = 0
    while i < len(takes):
        n, j = 1, i + 1
        while j < len(takes):
            if takes[i] < takes[j]: break
            n += 1
            j += 1
        answer.append(n)
        i += n
    return answer