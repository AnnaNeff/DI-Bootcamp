def render(board):
    border = "*" * 13
    sep = "*---|---|---*"
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

# ----- ВВОД ИГРОКА (как по условию: player_input(player)) -----
def player_input(player: list):
    mark = input('Enter "X" or "O" to choose player: ').strip().upper()
    row  = input(f'Enter row number (1-3) to put "{mark}": ').strip()
    col  = input(f'Enter column number (1-3) to put "{mark}": ').strip()
    player.clear()
    player.extend([mark, row, col])
    return player

# ----- ХОД: обновляем МОДЕЛЬ ПОЛЯ, а не строку -----
def game_function(board: list[list[str]], player: list[str]):
    mark, row_s, col_s = player
    r = int(row_s) - 1
    c = int(col_s) - 1
    if not (0 <= r < 3 and 0 <= c < 3):
        print("Out of range 1..3")
        return False
    if board[r][c] != " ":
        print("Cell already taken")
        return False
    board[r][c] = mark
    return True

# ----- ИГРА -----
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

print("GAME START!")
print(render(board))

player = []
player_input(player)        # наполняем ['X', '1', '1'] и т.п.
game_function(board, player)

print("\nAfter move:")
print(render(board))