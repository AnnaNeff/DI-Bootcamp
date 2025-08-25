MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

rows = MATRIX_STR.splitlines() 
matrix = [list(row) for row in rows]

decoded_message = []
def add_simbol(n):
    for row in matrix:
        if n < len(row):
            ch = row[n]
            if ch.isalpha() or ch == " ":
                decoded_message.append(ch)

add_simbol(0)
add_simbol(1)
add_simbol(2)
add_simbol(3)
                
print("".join(decoded_message))