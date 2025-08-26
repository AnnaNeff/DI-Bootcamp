ex_board_line = ["*", "***", "*", "***", "*", "***", "*"]
cell_line = ["*", "   ", "|", "   ", "|", "   ", "*"]
int_board_line = ["*", "---", "|", "---", "|", "---", "*"]


def display_board():

    field_line = []
    field_line.append(ex_board_line)
    field_line.append(cell_line)
    field_line.append(int_board_line)
    field_line.append(cell_line)
    field_line.append(int_board_line)
    field_line.append(cell_line)
    field_line.append(ex_board_line)
    field1 = [''.join(row) for row in field_line]
    field = '\n'.join(field1)
    return field

field = display_board()

display_board()
print(f"GAME START!\n{field}")    


player = []

def player_input(player:list):
    
    chose_player = input('Enter "X" or "O" to choose player: ')
    player.append(chose_player)
    choose_line = input(f'Enter line numer to put "{chose_player}": ')
    player.append(choose_line)
    choose_colum = input(f'Enter colum numer to put "{chose_player}": ')
    player.append(choose_colum)
    
    return player
    
player_input(player)

def game_function(field:list, player):
    mark, row_s, col_s = player
    if row_s == 1:
        r = int(1)
    elif row_s == 2:
        r = int(3)  
    elif row_s == 3:  
        r = int(5)
    else:
        print(f'You should choose correct line number')
    
    if col_s == 1:
        c = int(1)
    elif col_s == 2:
        c = int(3) 
    elif col_s == 3:  
        c = int(5)
    else:
        print(f'You should choose correct line number')

    mark.replace(list(field[r][c]))
    


game_function(field, player)


print(field)




