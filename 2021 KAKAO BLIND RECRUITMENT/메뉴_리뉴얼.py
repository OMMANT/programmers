from itertools import combinations

def solution(orders, course):
    order_count = {}    
    answer = []
    
    for order in orders:
        for alpha in order:
            order_count[alpha] = 1 if alpha not in order_count.keys() else order_count[alpha] + 1
    keys = []
    for idx, value in enumerate(order_count.values()):
        if value > 1:
            keys.append(list(order_count.keys())[idx])
    for menu in course:
        selections = list(combinations(keys, menu))
        selection_count = []
        for selection in selections:
            count = 0
            for order in orders:
                flag = True
                for selected_menu in selection:
                    if selected_menu not in order:
                        flag = False
                        break
                if flag:
                    count += 1
            selection_count.append(count)
        if len(selection_count) < 1 or max(selection_count) < 2:
            continue
        max_count = max(selection_count)
        for idx, selection in enumerate(selections):
            if selection_count[idx] == max_count:
                answer.append(''.join(sorted(selection)))
        
    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
