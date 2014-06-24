def NextPalindrome(a):
	l = len(a)
	mid = int(l/2)
	i = 0
	allNines = False
	while i < l :
		if a[i]== '9':
			i+=1
			allNines = True
		else:
			allNines = False
			break
	if allNines:
		return AllNines(l)
    
	isPalindrome = False
	if l%2 == 1:
		while i < mid:
			if(a[mid - i] == a[mid + i]):
				i+=1
			else:
				break
        
		if i == mid:
			isPalindrome = True
	else:
		while i < mid:
			if(a[mid - i-1] == a[mid + i]):
				i+=1
			else:
				break
		if i == mid:
			isPalindrome = True
    
	if isPalindrome :
		a = NextPalindromeOfPalindrome(a)
	else:
		prevA = a
		a = NextPalindromeOfNonPalindrome(a,i,l)
		if int(prevA) > int(a):
			a = NextPalindromeOfPalindrome(a,l)
    
	return a

def AllNines(l):
	a = ['1']
	for i in range(l-1):
		a.append('0')
	a.append('1')
	return "".join(a)

def NextPalindromeOfNonPalindrome(a,i,l):
	a = list(a)
	mid = int(l/2)
	if l%2 == 1 :
		while i < mid:
			a[mid + i] = a[mid - i]
			i+=1
	else :
		while i < mid:
			a[mid + i] = a[mid -1 - i]
			i+=1
	return "".join(a)



def NextPalindromeOfPalindrome(a,length):
	
	a = list(a)
	mid = int(length/2)
	if length % 2 == 1:
		if a[mid] != '9' :
			a[mid] = str(int(a[mid]) + 1)
		else :
			val = a[mid -1 ] + a[mid] + a[mid + 1]
			newStr = str(int(val) + 101)
			a[mid] = '0'
			a[mid -1 ] = newStr[2]
			a[mid + 1] = newStr[0]
	else:
		val = a[mid-1]+a[mid]
		newStr = str(int(val)+11)
		a[mid-1] = newStr[0]
		a[mid] = newStr[1]
    
	return "".join(a)


number = input()
inp = []
for i in xrange(number):
	inp.append(raw_input())
for i in xrange(number):
	print NextPalindrome(inp[i])

