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
    field = [''.join(row) for row in field_line]
    print('\n'.join(field))

print("GAME START!")    
display_board()