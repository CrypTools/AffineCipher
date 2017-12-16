import string

def decrypt():
  initial = input('Donnes le message à décrypter : ')
  cle = input("Donnes la clé : ")
  quotients = cle.split("-")
  initial = initial.lower()
  numeros = []
  for character in initial:
      numeros.append(ord(character) - 97)
  
  a = int(input('Donnes le nombre a utilisé : '))
  b = int(input('Donnes le nombre b utilisé : '))
  
  output = ""
  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))

  for i in range(len(numeros)):
    image = str(alphabet[int(((int(quotients[i]) * 26 + numeros[i] - b) / a))])
    output += image
    
  print(output)
