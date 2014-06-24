
def printPrimes(ListOfItems, m,n):
	if (n < len(ListOfItems)):
		for i in xrange(m,n):
			if(ListOfItems[i]):
				print i
		return ListOfItems
	ListOfItems = []
	for i in xrange(n+1):
		ListOfItems.append(True)
	maxIvalue = int(n**0.5)
	for i in xrange(2,maxIvalue +1):
		if ListOfItems[i] == True:
			j = i*i
			while j < n:
				ListOfItems[j] = False
				j += i
	for i in xrange(m,n):
		if(ListOfItems[i]):
			print i
	return ListOfItems

ListOfItems = []
t = input()
for i in range(t):
	s = raw_input().split(" ")
	ListOfItems = printPrimes(ListOfItems, int(s[0]),int(s[1]))
	print ""