import numpy as np
from heapq import heappop, heappush

adj_list = []
def solution(n, s, a, b, fares):
    global adj_list
    adj_list = [{} for i in range(n + 1)]

    for fare in fares:        
        start, end, cost = fare
        adj_list[start][end] = cost
        adj_list[end][start] = cost

    answer = dijkstra(s, a) + dijkstra(s, b)
    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return int(answer)

def dijkstra(src, dst):
    global adj_list
    n = len(adj_list)
    distance = [np.inf for i in range(n)]
    distance[src] = 0
    pq = [[0, src]]

    while pq:
        w, x = heappop(pq)

        if distance[x] < w: continue

        for key in adj_list[x].keys():
            ncost = adj_list[x][key]
            ncost += w
            if ncost < distance[key]:
                distance[key] = ncost
                heappush(pq, [ncost, key])
    
    return distance[dst]

n = [6, 7, 6]
s = [4, 3, 4]
a = [6, 4, 5]
b = [2, 1, 6]
fares = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
]

for nn, ss, aa, bb, faress in zip(n, s, a, b, fares):
    print(solution(nn, ss, aa, bb, faress))
    