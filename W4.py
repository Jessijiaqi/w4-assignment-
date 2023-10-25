def flood_fill(input_board, old, new, x, y):
    def fill(x, y):
        if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]) or input_board[x][y] != old:
            return
        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]
        fill(x - 1, y)  
        fill(x + 1, y)  
        fill(x, y - 1)  
        fill(x, y + 1)  
    if 0 <= x < len(input_board) and 0 <= y < len(input_board[0]) and input_board[x][y] == old:
        fill(x, y)  
    return input_board
board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
for row in modified_board:
    print(row)

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

modified_board = flood_fill(input_board=board, old=".", new="~", x=1, y=1)
for row in modified_board:
    print(row)
