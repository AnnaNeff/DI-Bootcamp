from utils import unzip_with_7z

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------
password_is_guessed = False

for letter1 in 'abcdefghijklmnopqrstuvwxyz':
    for letter2 in 'abcdefghijklmnopqrstuvwxyz':
      find_me = letter1 + letter2
      secret_password = find_me + 'bcmpda'
      
      print(f"Checking password: {secret_password}")
      
      if unzip_with_7z(zip_file_path, dest_path, secret_password) == True:
          password_is_guessed = True
          break
    
    if password_is_guessed == True:
       print("SUCCESS!")
       break
