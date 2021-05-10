from itertools import combinations

def solution(orders, course):
    #ex) course: [2, 3, 4]
    answer = []

    for number in course:
        # n == 2
        # orders: ["ABCFG", "AC", ...]
        set_menu = {}
        for order in orders:
            # order: "ABCFG"
            if len(order) >= number:
                selections = combinations(order, number)
                for selection in selections:
                    select = ''.join(sorted(selection))
                    set_menu[select] = 1 if select not in set_menu.keys() else set_menu[select] + 1
        if len(set_menu.keys()) < 1 or max(set_menu.values()) < 2:
            continue
        max_count = max(set_menu.values())
        for key in set_menu.keys():
            if set_menu[key] == max_count:
                answer.append(key)
    
    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
