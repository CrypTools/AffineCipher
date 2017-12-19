import string

def decrypt():
  initial = input('Give the message (no space or special characters) : ')
  cle = input("Give the key : ")
  quotients = cle.split("-")
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  
  a = int(input('Give the value of a : '))
  b = int(input('Give the value of b : '))
  
  output = ""
  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))

  for i in range(len(numeros)):
    image = str(alphabet[int(((int(quotients[i]) * 26 + numeros[i] - b) / a))])
    output += image
    
  print("Decrypted message : " + output)
