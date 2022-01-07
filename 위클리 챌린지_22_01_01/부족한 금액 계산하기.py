def solution(price, money, count):   
    return price * count * (count + 1) // 2 - money

if __name__ == '__main__':
    price = 3
    money = 20
    count = 4

    print(solution(price, money, count))