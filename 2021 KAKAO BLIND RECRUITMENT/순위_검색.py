from itertools import combinations

def solution(info, query):
    data = {}
    answer = []
    combination = []

    for i in range(1, 5):            
        combination += list(combinations(range(4), i))

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
    
    for q in query:
        q = q.replace('and', '').replace('  ', ' ').split()
        score = int(q.pop())
        count = 0
        q = ''.join(q)
        try:
            for scores in data[q]:
                if scores >= score:
                    count += 1
            answer.append(count)
        except KeyError:
            answer.append(0)

    return answer
        

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
