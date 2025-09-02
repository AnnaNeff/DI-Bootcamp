import os

dir_path = os.path.dirname(os.path.realpath(__file__))
#PYTHON I/O

# try:
#     f =  open('secrets.txt')
#     secret_data = f.read()
#     print(secret_data)

# except:
#     raise ValueError
# finally:
#     f.close()

#MODERN WAY

# with open(f'{dir_path}/secrets.txt', 'a', encoding = 'utf-8') as f:
#     # file_content = f.read() #(ONLY FOR READ)
#     f.write('\nblablae')
#     print("success")


with open(f'{dir_path}/starwars.txt', 'r', encoding = 'utf-8') as f:
    # file_content = f.readlines()[0:5]
    # print(file_content)
    
    # file_content = f.readline(5)
    # print(file_content)

    # for line in f:
        print(f.readlines()[9])
        print('end if the document')

with open(f'{dir_path}/starwars.txt', 'r', encoding = 'utf-8') as f:
        print(f.readline(5))
        print('end if the document')


