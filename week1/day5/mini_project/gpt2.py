# Поле 3x3: модель игры (пока пустые клетки)
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def display_board(board):
    # Собираем ASCII-сетку из содержимого board и возвращаем строку
    border = "*" * 13
    sep    = "*---|---|---*"
    lines = [
        border,
        f"* {board[0][0]} | {board[0][1]} | {board[0][2]} *",
        sep,
        f"* {board[1][0]} | {board[1][1]} | {board[1][2]} *",
        sep,
        f"* {board[2][0]} | {board[2][1]} | {board[2][2]} *",
        border,
    ]
    return "\n".join(lines)

# По условию: функция должна принимать список player и модифицировать его
player = []

def player_input(player):
    # Выбор метки игрока
    mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    # Координаты клетки (1..3)
    row  = input(f'Enter row number (1-3) to put "{mark}": ').strip()
    col  = input(f'Enter column number (1-3) to put "{mark}": ').strip()
    # Сохраняем в переданный список
    player.clear()
    player.extend([mark, row, col])
    return player

def game_function(board, player):
    # Ставим метку игрока в модель board
    mark, row_s, col_s = player
    r = int(row_s) - 1   # переводим 1..3 -> 0..2
    c = int(col_s) - 1
    if board[r][c] == " ":
        board[r][c] = mark
    else:
        print("Cell already taken")  # простая проверка занятости

print("GAME START!")
print(display_board(board))   # печатаем пустое поле

player_input(player)          # например: ['X','1','1']
game_function(board, player)  # обновляем поле по ходу

print("\nAfter move:")
print(display_board(board)) 