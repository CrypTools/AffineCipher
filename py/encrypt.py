# ==============================================================================
#
#    Use:
#    encrypt("Hello World!", 9, 13)
#    => "Yxiij Djkio!"
#
# ==============================================================================

def encrypt(s, a, b):

	output = ''

	for c in s:
		
		if ord(c) >= 0x41 and ord(c) <= 0x5a:
			i = ord(c) - 0x41
			i = ( i * a + b ) % 26
			output += chr(i + 0x41)

		elif ord(c) >= 0x61 and ord(c) <= 0x7a:
			i = ord(c) - 0x61
			i = ( i * a + b ) % 26
			output += chr(i + 0x61)

		else:
			output += c

	return output

if __name__ == "__main__":
	print( encrypt("Hello World!", 9, 13) )
