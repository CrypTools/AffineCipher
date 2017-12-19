import string

def decrypt(initial, cle, a, b):
  
  """  Use: decrypt("message", 45, 65)
=> Encrypted message : hlrrnxl
=> Key : 23-9-33-33-2-12-9
"""

  quotients = cle.split("-")
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  output = ""
  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))

  for i in range(len(numeros)):
    image = str(alphabet[int(((int(quotients[i]) * 26 + numeros[i] - b) / a))])
    output += image
    
  print(output)
