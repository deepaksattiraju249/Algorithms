'''
By listing the first six prime numbers: 2,3,5,7,11 and 13, we can see that the 6th prime is 13.
What is the N'th prime number?

Input Format 
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Output Format 
Print the required answer for each test case.

Constraints 
1≤T≤103 
1≤N≤104

Sample Input
2
3
6

Sample Output
5
13
'''

def getPrimes(listOfPrimes, m,n):
	if (n < len(listOfPrimes)):
		for i in xrange(m,n):
			if(listOfPrimes[i]):
				print i
		return listOfPrimes
	listOfPrimes = []
	for i in xrange(n+1):
		listOfPrimes.append(True)
	maxIvalue = int(n**0.5)
	for i in xrange(2,maxIvalue +1):
		if listOfPrimes[i] == True:
			j = i*i
			while j < n:
				listOfPrimes[j] = False
				j += i
	x = []
	for i in xrange(m,n):
		if(listOfPrimes[i]):
			x.append(i)
	return x

listOfPrimes = getPrimes([], 1,10**6)

t = input()
for _ in xrange(t):
    print listOfPrimes[input()]


