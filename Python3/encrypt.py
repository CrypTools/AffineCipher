"""
Use : encrypt("message", 56, 89)
=> 'hbffljb'
"""

import string

def encrypt(initial, a, b):
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  output = ""
  key = ""

  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))
  for i in range(len(numeros)):
    image = str(alphabet[int(numeros[i] * a + b) % 26])
    output += image
    
    div = str(int(numeros[i] * a + b) // 26)
    if i == 0:
      divtem = div
    else:
      divtem = "-" + div

    key += divtem
  
  return output
  return key
