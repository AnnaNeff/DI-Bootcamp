board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

che

def display_board(board):
    border = "*" * 13
    sep =  "*---|---|---*"
    lines = [
        border,
        f"* {board[0][0]} | {board[0][1]} | {board[0][2]} *",
        sep,
        f"* {board[1][0]} | {board[1][1]} | {board[1][2]} *",
        sep, 
        f"* {board[2][0]} | {board[2][1]} | {board[2][2]} *",
        border
    ]
    
    return "\n".join(lines)

player = []
print("GAME START")

def player_input(player: list):
    print(display_board(board))

    # очистим список, чтобы в нём всегда были только текущие 3 значения
    player.clear()
    
    mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    while mark not in ("X", "O"):
        print("Please enter X or O.")
        mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    player.append(mark)
    
    row_s = input(f'Enter line numer to put "{mark}" (1 - 3): ').strip()
    while row_s not in "123":
        print("You should choose correct option (1 -3): ")
        row_s = input(f'Enter line numer to put "{mark}" (1 - 3): ').strip()
    player.append(row_s)
    
    col_s = input(f'Enter colum numer to put "{mark}" (1 - 3): ').strip()
    while col_s not in "123":
        print("You should choose correct option (1 -3): ")
        col_s = input(f'Enter colum numer to put "{mark}" (1 - 3): ').strip()
    player.append(col_s)
    
def check_win(board, player):
    



def game_function(board, player):
    mark, row_s, col_s = player
    r = int(row_s) -1
    c = int(col_s) -1
    if board[r][c] == " ":
        board[r][c] = mark
    else:
        print("Cell already taken")

while True:
    player_input(player)
    game_function(board, player)
