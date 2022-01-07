from itertools import product

def solution(word):
    dictionary = sorted([''.join(p) for i in range(1, 6) for p in product('AEIOU', repeat=i)])
    
    return dictionary.index(word) + 1

if __name__ == '__main__':
    words = [
        'AAAAE',
        'AAAE',
        'I',
        'EIO'
    ]
    for word in words:
        print(solution(word))