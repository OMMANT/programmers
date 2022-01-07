from collections import defaultdict

def dfs(root):
    global tree, count
    visited = []
    stack = [root]
    while stack:
        root = stack.pop()
        if root not in visited:
            visited.append(root)
            stack += tree[root]
            count += 1

def solution(n, wires):
    global tree, count
    min_diff = n

    for i in range(len(wires)):
        d_wires = wires[:]
        del d_wires[i]
        count = 0
        tree = defaultdict(list)
        for wire in d_wires:
            tree[wire[0]].append(wire[1])
            tree[wire[1]].append(wire[0])
        dfs(list(tree.keys())[0])
        min_diff = min(min_diff, abs(n - 2*count))

    return min_diff

if __name__ == '__main__':
    ns = [9, 4, 7]
    wireses = [
        [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],
        [[1,2],[2,3],[3,4]],
        [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
    ]

    for n, wires in zip(ns, wireses):
        print(solution(n, wires))