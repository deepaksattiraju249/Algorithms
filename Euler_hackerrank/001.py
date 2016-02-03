'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

Input Format 
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Output Format 
For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

Constraints 
1≤T≤105 
1≤N≤109

Sample Input

2
10
100

Sample Output

23
2318
'''

def sum_of(n):
    return n*(n+1) /2

t = input()
for _ in xrange(t):
    n = input() -1
    n3 = n/3
    n5 = n/5
    n15 = n/15
    
    print 3*sum_of(n3) + 5*sum_of(n5) - 15*sum_of(n15)