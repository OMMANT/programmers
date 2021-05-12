import numpy as np

def solution(info, query):
    data = []
    answer = []

    for datum in info:
        datum = datum.split()
        datum[-1] = int(datum[-1])
        datum = np.array(datum)
        data.append(datum)
    data = np.array(data)
    
    for q in query:
        q = q.split(' and ')
        temp = q[-1].split()   
        del q[-1]
        q = np.array(q + temp)
        
        mask = np.array([True] * data.shape[0])
        for i in range(4):
            if q[i] == '-':
                pass
            else:
                mask = mask & (q[i] == data[:, i])
        if q[4] == '-':
            pass
        else:
            q[4] = int(q[4])
            mask = mask & (int(q[4]) <= data[:, 4].astype(np.int))
        answer.append(len(data[mask]))

    return answer
        

print(solution(
    ['java backend junior pizza 150', 'python frontend senior chicken 210', 'python frontend senior chicken 150', 'cpp backend senior pizza 260', 'java backend junior chicken 80', 'python backend senior chicken 50'],
    ['java and backend and junior and pizza 100', 'python and frontend and senior and chicken 200', 'cpp and - and senior and pizza 250', '- and backend and senior and - 150', '- and - and - and chicken 100', '- and - and - and - 150']))
