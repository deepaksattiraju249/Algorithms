n = input()
ListOfItems = []
for i in xrange(n+1):
	ListOfItems.append(True)
print ListOfItems
maxIvalue = int(n**0.5)
print maxIvalue
for i in xrange(2,maxIvalue +1):
	print i
	if ListOfItems[i] == True:
		print "reached here"
		j = i*i
		while j < n:
			#print j 
			ListOfItems[j] = False
			j += i
print ListOfItems

for i in xrange(2,n):
	if(ListOfItems[i]):
		print i
