board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

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

def player_input(player: list):
    print(display_board(board))

    player.clear()
    
    mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    while mark not in ("X", "O"):
        print("🤌 Please enter X or O.")
        mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    player.append(mark)
    
    row_s = input(f'Enter line numer to put "{mark}" (1 - 3): ').strip()
    while row_s not in "123":
        print("🤌 You should choose correct option (1 -3): ")
        row_s = input(f'Enter line numer to put "{mark}" (1 - 3): ').strip()
    player.append(row_s)
    
    col_s = input(f'Enter colum numer to put "{mark}" (1 - 3): ').strip()
    while col_s not in "123":
        print("🤌 You should choose correct option (1 -3): ")
        col_s = input(f'Enter colum numer to put "{mark}" (1 - 3): ').strip()
    player.append(col_s)
    

def game_function(board, player):
    mark, row_s, col_s = player
    r = int(row_s) -1
    c = int(col_s) -1
    if board[r][c] == " ":
        board[r][c] = mark
    else:
        print("❌ Cell already taken")


def check_win(board):
    # строки
    for r in range(3):
        if board[r][0] != " " and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]
    # столбцы
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # диагонали
    if board[1][1] != " ":
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None

def is_tie(board):
    
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                return False
    return True


def play():
    print("GAME START")
    while True:
        player_input(player)
        game_function(board, player)
        
        winner = check_win(board)
        if winner is not None:
            print(display_board(board))
            print(f"{winner} wins! 🎉")
            break

        if is_tie(board):
            print(display_board(board))
            print("It's a tie! 🤝")
            break
        
play() 