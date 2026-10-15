"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2276/A ------------------------------------

Monocarp has a slices of cheese and b slices of sausage. He wants to make the maximum possible number of sandwiches for his friends from them.

Monocarp is very thrifty, so he must use all a slices of cheese and all b slices of sausage without any leftovers to make the sandwiches. 
In addition, he has the following rules for making sandwiches:

each sandwich must contain at least one slice of cheese and at least one slice of sausage;
each of the a slices of cheese and each of the b slices of sausage must be placed on exactly one sandwich;
for each sandwich, the number of slices of cheese must be strictly greater than the number of slices of sausage.
Help Monocarp determine the maximum number of sandwiches he can make, or determine that it is impossible to distribute all slices according to these rules.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The only line of each test case contains two integers a and b (1 ≤ a, b ≤ 100) — the number of slices of cheese and sausage, respectively.

Output
For each test case, print one integer — the maximum number of sandwiches that can be made. 
If it is impossible to distribute all pieces according to the described rules, print −1 instead.

Input:
3
6 4
5 1
4 5

Output:
2
1
-1
"""
cases = int(input())
for _ in range(cases):
    a, b = map(int, input().split())
    if(a <= b):
        print(-1)
    elif(a >= (2 * b)):
        print(b)
    else:
        print(a - b)