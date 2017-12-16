import string

def encrypt():
  initial = input('Give the message (no space or special characters) : ')
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)

  a = int(input('Give a (integer greater than or equal to 0) : '))
  b = int(input('Give b (integer greater than or equal to 0) : '))

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
