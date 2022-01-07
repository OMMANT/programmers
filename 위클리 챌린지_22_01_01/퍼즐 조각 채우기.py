from copy import deepcopy
from operator import itemgetter
import numpy as np

def get_block(board, i, j, target=1):
    block = []
    visited = []
    stack = [(i, j)]
    
    while stack:
        x, y = stack.pop()
        if (x, y) not in visited and board[x][y] == target:
            visited.append((x, y))
            block.append((x - i, y - j))
            for a, b in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                if 0 <= x + a < len(board) and 0 <= y + b < len(board[0]): stack.append((x + a, y + b))
    
    return block

def block2square(blocks):
    squared = []

    for block in blocks:
        x = 'map(itemgetter(0), block)'
        y = 'map(itemgetter(1), block)'
        min_x, max_x = min(eval(x)), max(eval(x))
        min_y, max_y = min(eval(y)), max(eval(y))
        square = np.zeros((max_x - min_x + 1, max_y - min_y + 1)).astype(int).tolist()
        for x, y in block:
            square[x + abs(min_x)][y + abs(min_y)] = 1
        squared.append(square)

    return squared

def rotate(table):
    rotated = [[(-y, x) for x, y in block] for block in table]

    return rotated

def solution(game_board, table):
    answer = 0
    copy_board = deepcopy(game_board)
    copy_table = deepcopy(table)
    board_blocks = []
    table_blocks = []
    for i in range(len(copy_board)):
        for j in range(len(copy_board[0])):
            if copy_board[i][j] == 0:
                block = get_block(copy_board, i, j, target=0)
                for x, y in block: copy_board[i + x][j + y] = 1
                board_blocks.append(block)
    for i in range(len(copy_table)):
        for j in range(len(copy_table[0])):
            if copy_table[i][j] == 1:
                block = get_block(copy_table, i, j)
                for x, y in block: copy_table[i + x][j + y] = 0
                table_blocks.append(block)
    sqaured_board = block2square(board_blocks)
    for _ in range(4):
        delete = []
        sqaured_table = block2square(table_blocks)
        for index, block in enumerate(sqaured_table):
            if block in sqaured_board:
                for i in range(len(block)):
                    for j in range(len(block[0])):
                        if block[i][j] == 1: answer += 1
                delete.append(index)
                del sqaured_board[sqaured_board.index(block)]
        for index in delete[::-1]: del table_blocks[index]
        table_blocks = rotate(table_blocks)

    return answer

if __name__ == '__main__':
    game_boards = [
        [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
        [[0,0,0],[1,1,0],[1,1,1]]
    ]
    tables = [
        [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,0,0,0],[0,1,0,0,0,0]],
        [[1,1,1],[1,0,0],[0,0,0]]
    ]

    for game_board, table in zip(game_boards, tables):
        print(solution(game_board, table))