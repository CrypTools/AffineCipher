import string

def decrypt(initial, key, a, b):
  """ Use : decrypt("hbffljb", "29-12-42-42-3-16-12", 56, 89)
=> 'message'
  """
  quotient = key.split("-")
  initial = initial.lower()
  list = []
  for character in initial:
      list.append(ord(character) - 97)
  output = ""
  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))

  for i in range(len(list)):
    image = str(alphabet[int(((int(quotient[i]) * 26 + list[i] - b) / a))])
    output += image
    
  return output
