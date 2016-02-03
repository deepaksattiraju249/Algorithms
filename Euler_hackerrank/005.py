'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?

Input Format 
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Output Format 
Print the required answer for each test case.

Constraints 
1≤T≤10 
1≤N≤40

Sample Input

2
3
10
Sample Output

6
2520
'''

def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)

def range_lcm(r):
    n = 1
    for i in xrange(1, r+1):
        n = lcm(n, i)
    return n

t = input()
for _ in xrange(t):
    print range_lcm(input())