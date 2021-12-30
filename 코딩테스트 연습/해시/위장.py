def solution(clothes):
    answer = 1
    cloth = {}
    
    for name, kind in clothes:        
        # Add kind and set the number of cloth as 1
        # The name of cloth never same -> Just save the number
        if kind in cloth.keys(): cloth[kind] += 1
        else: cloth[kind] = 2
    
    for v in cloth.values():
        answer *= v

    return answer - 1

if __name__ == '__main__':
    clothes = [
        [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]], 
        [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    ]
    for clothe in clothes:
        print(solution(clothe))
        