def encrypt(initial, a, b):
  """ Use : encrypt("message", 56, 89)
=> ('hbffljb', '29-12-42-42-3-16-12')
  """
  initial = initial.lower()
  mylist = []
  for character in initial:
      mylist.append(ord(character) - 97)
  output = ""
  key = ""

  alphabet = dict(zip(range(0, 26), string.ascii_lowercase))
  for i in range(len(mylist)):
    image = str(alphabet[int(mylist[i] * a + b) % 26])
    output += image
    
    div = str(int(mylist[i] * a + b) // 26)
    if i == 0:
      divtem = div
    else:
      divtem = "-" + div

    key += divtem
  
  return output, key
