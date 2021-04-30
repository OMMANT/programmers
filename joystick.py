def solution(name):
    new_name = []
    answer = 0
    cidx = 0
    for c in name:
        new_name.append(ord(c) - ord('A'))
    while new_name != [0] * len(new_name):
        lidx, ridx = 1, 1
        # Change current idx to A
        if new_name[cidx] >= 13:
            answer += 26 - new_name[cidx]
        else:
            answer += new_name[cidx]
        new_name[cidx] = 0
        if new_name != [0] * len(new_name):
            break
        for i in range(1, len(new_name)):
            is_break = False
            if new_name[cidx + i] == 0:
                ridx += 1
            else:
                is_break = True
            if new_name[cidx - i] == 0:
                lidx += 1
            else:
                is_break = True
            if is_break:
                break
        if ridx > lidx:
            answer += lidx
            cidx -= lidx
        else:
            answer += ridx
            cidx += ridx
    return answer