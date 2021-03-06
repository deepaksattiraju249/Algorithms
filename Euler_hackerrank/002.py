'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1,2,3,5,8,13,21,34,55,89,⋯
By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.

Input Format 
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Output Format 
Print the required answer for each test case.

Constraints 
1≤T≤105 
10≤N≤4×1016

Sample Input

2
10
100

Sample Output

10
44

'''


ref = {}
def fib(n):
    global ref
    if ref.get(n,0) > 0:
        return ref[n]
    else:
        if n == 0 or n == 1:
            return n
        nex = fib(n-1) + fib(n-2)
        ref[n] = nex
        return nex
sums = {}
t = input()
for _ in xrange(t):
    x = input()
    al = 0
    n = 0
    f = fib(n)
    
    prevKey = None
    
    for key in sums:
        if key > x:
            break
        prevKey = key
        
    if prevKey != None:
        al,n = sums[prevKey]
        f = fib(n)
    while f < x:
        if f %2 == 0:
            al += f
        
        n +=1
        f = fib(n)
        
    sums[f] = (al,n)
    print al
