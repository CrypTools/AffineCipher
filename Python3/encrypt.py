

import string

def encrypt(initial, a, b):
  """
  bobuobu
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

  print("Message crypté : " + output)
  print("\n" + "Clé : " + cle)
