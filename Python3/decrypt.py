"""
Use : decrypt("hbffljb", "29-12-42-42-3-16-12", 56, 89)
=> 'message'
"""

import string

def decrypt(initial, key, a, b):
  quotients = key.split("-")
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  output = ""
  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))

  for i in range(len(numeros)):
    image = str(alphabet[int(((int(quotients[i]) * 26 + numeros[i] - b) / a))])
    output += image
    
  return output
