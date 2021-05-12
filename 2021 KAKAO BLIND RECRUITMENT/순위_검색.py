from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    data = {}
    answer = []
    combination = [
        [0], [1], [2], [3],
        [0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3],
        [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3],
        [0, 1, 2, 3]
    ]

    # Add Data
    for datum in info:
        datum = datum.split()
        score = datum.pop()
        d = ''.join(datum)
        try:
            data[d].append(int(score))
        except KeyError:
            data[d] = [int(score)]
        
        for c in combination:
            dat = datum.copy()
            for i in c:
                dat[i] = '-'
            dat = ''.join(dat)
            try:
                data[dat].append(int(score))
            except KeyError:
                data[dat] = [int(score)]

    for key in data.keys():
        data[key].sort()
    
    for q in query:
        q = q.replace('and', '').replace('  ', ' ').split()
        score = int(q.pop())
        q = ''.join(q)
        try:
            size = len(data[q])
            answer.append(size - bisect_left(data[q], score, lo=0, hi=size))
        except KeyError:
            answer.append(0)

    return answer
        

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
