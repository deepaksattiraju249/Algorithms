'''
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which,
a2+b2=c2
For example, 32+42=9+16=25=52
Given N, Check if there exists any Pythagorean triplet for which a+b+c=N 
Find maximum possible value of abc among all such Pythagorean triplets, If there is no such Pythagorean triplet print −1.

Input Format 
The first line contains an integer T i.e. number of test cases. 
The next T lines will contain an integer N.

Output Format 
Print the value corresponding to each test case in separate lines.

Constraints 
1≤T≤3000 
1≤N≤3000

Sample Input
2
12
4

Sample Output
60
-1

'''

def find_abc(n):
    ans = -1
    if not(n%3==0 or n%2==0):
        return -1
    for a in xrange(1,n/3):
        for b in xrange(a+1,n/2):
            c = n-a-b
            if(a**2+b**2 == c**2):
                ans = max(ans,a*b*c)
    return ans

t = input()
for _ in xrange(t):
    print find_abc(input())
#Timed Out for 3 test cases   