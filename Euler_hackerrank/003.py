'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of a given number N?

Input Format 
First line contains T, the number of test cases. This is followed by T lines each containing an integer N.

Output Format 
For each test case, display the largest prime factor of N.

Constraints 
1≤T≤10 
10≤N≤1012

Sample Input

2
10
17

Sample Output

5
17

'''



def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

t = input()
for _ in xrange(t):
    print largest_prime_factor(input())