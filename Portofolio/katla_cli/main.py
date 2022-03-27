import random
import re

class katla:
  def __init__(self):
    self.list_keyword = [
      'rumah',
      'putih',
      'merah',
      'ramah',
      'premi',
      'perah',
      'angka',
      'huruf',
      'cermat',
      'keris',
    ]
    self.selected_keyword = ''
    self.count_attempt = 1
    self.already_guessed = False

  # Mengambil random keyword dari list
  def get_random_keyword(self):
    self.selected_keyword = random.choice(self.list_keyword)
  
  def check_keyword(self, keyword):
    # Cek apakah keyword terdiri dari 5 char
    if len(keyword) != 5:
      print("input harus 5 huruf")
      return False
    
    self.count_attempt = self.count_attempt + 1
    
    # Ambil hanya alfabet dan ubah jadi lowercase
    keyword = re.sub(r'[^a-zA-Z]', '', keyword).lower()

    # Cek apakah letter terdapat pada 
    print('Tebakan')
    for index, letter in enumerate(keyword):
      if(letter == self.selected_keyword[index]):
        print(f'\033[92m{letter}\033[0m', end=" ")
        
      elif letter in self.selected_keyword:
        print(f'\033[93m{letter}\033[0m', end=" ")
        
      else:
        print(f'{letter}', end=" ")
        
    print('')

    # Cek apakah keyword benar
    if keyword == self.selected_keyword:
      return True

  def main(self):
    self.get_random_keyword()
    while self.count_attempt < 7 :
      print(f'\nPercobaan ke {self.count_attempt}')
      self.already_guessed = self.check_keyword(input('Input Kata :'))
      if self.already_guessed:
        break
    
    if self.already_guessed:
      print(f'Selamat, anda berhasil menebak pada percobaan ke-{self.count_attempt}. \ndan kata yang benar adalah {self.selected_keyword}')
    else:
      print(f'Yahh, anda tidak berhasil menebak. \nkata yang benar adalah "{self.selected_keyword}"')
    print('Game Berhenti')
    
dating_app = katla()
dating_app.main()