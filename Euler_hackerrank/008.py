'''
Find the greatest product of K consecutive digits in the N digit number.

Input Format 
First line contains T that denotes the number of test cases. 
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer. 

Output Format 
Print the required answer for each test case.

Constraints 
1≤T≤100 
1≤K≤7 
K≤N≤1000

Sample Input
2
10 5
3675356291
10 5
2709360626

Sample Output
3150
0

'''

def find_product(num):
    if 0 in num:
        return 0
    prod = 1
    for d in num:
        prod*=d
    return prod
    
t = input()
for _ in xrange(t):
    n,k = [int(x) for x in raw_input().split(" ")]
    digits = [int(ch) for ch in raw_input()]
    ans = 0
    for i in xrange(n-k):
        ans = max(ans,find_product(digits[i:i+k]))
    print ans