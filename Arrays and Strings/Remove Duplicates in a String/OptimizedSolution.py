#In this we wont create an extra set or an array
#assuming the characters in the text to be a-z


def removeDuplicates(s):			#this method doesnt retain the order in which the characters are in the string
	val = 0 # marking all bits to be 0 ie no characeter is encountered
	for ch in s:
		val |= 2**(ord(ch) - ord('a')) # making that bit as 1 in val if that character whose ascii val (- the 'a' ascii value to bring it in the range of 1-26) is countered 
	final = ""
	for i in range(32):
		if 2**i & val > 0 :
			final += chr(i + 97)
	return final




print removeDuplicates("")
print removeDuplicates("abadacada")