# ==============================================================================
#
#    Use:
#    decrypt("Yxiij Djkio!", 9, 13)
#    => "Hello World!"
#
# ==============================================================================

def decrypt(s, a, b):

	output = ''

	a_inv = 0
	while a * a_inv % 26 != 1:
		a_inv += 1

	for c in s:
		
		if ord(c) >= 0x41 and ord(c) <= 0x5a:
			i = ord(c) - 0x41
			i = ( a_inv * (i-b) ) % 26
			output += chr(i + 0x41)

		elif ord(c) >= 0x61 and ord(c) <= 0x7a:
			i = ord(c) - 0x61
			i = ( a_inv * (i-b) ) % 26
			output += chr(i + 0x61)

		else:
			output += c

	return output

if __name__ == "__main__":
	print( decrypt("Yxiij Djkio!", 9, 13) )
