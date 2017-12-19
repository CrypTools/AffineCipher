

import string

def encrypt(initial, a, b):
  
  """
  Use: encrypt("message", 45, 65)
=> Encrypted message : hlrrnxl
=> Key : 23-9-33-33-2-12-9
  """
  
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  output = ""
  cle = ""

  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))
  for i in range(len(numeros)):
    image = str(alphabet[int(numeros[i] * a + b) % 26])
    output += image
    
    div = str(int(numeros[i] * a + b) // 26)
    if i == 0:
      divtem = div
    else:
      divtem = "-" + div

    cle += divtem

  print("Encrypted message : " + output)
  print("\n" + "Key : " + cle)
