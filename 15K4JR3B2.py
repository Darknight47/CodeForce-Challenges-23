"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2284/A2 --------------------------

This is the hard version of the problem. The difference between the versions is that in this version, in one operation, a point coordinate changes by a power of two.

Unemployed ∗ Angel places three points A, B, and C at the origin, and also gives you an array a of length n.

You must perform exactly n operations. During the i-th operation, choose one of these points and increase or decrease one of its coordinates by 2ai. 
In other words, if the chosen point has coordinates (x,y), then in the i-th operation you may move it to (x+2ai,y), (x−2ai,y), (x,y+2ai), or (x,y−2ai).

Unemployed ∗ Angel asks you to find the maximum doubled area of triangle ABC after all operations are performed. As she is your idol, you cannot refuse her.

Since Unemployed ∗ Angel is very smart, she can show that the value of interest is always an integer.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 100). The description of the test cases follows.

The first line of each test case contains one integer n (2 ≤ n ≤ 100) — the length of array a and the number of operations.

The second line of each test case contains n integers a1,a2,…,an (0 ≤ ai ≤ 24) — the elements of array a.

Output
For each test case, output one integer — the maximum doubled area of triangle ABC.

Input:
4
2
0 0
3
0 0 1
6
0 1 2 2 4 0
6
24 24 24 0 0 0

Output:
1
4
192
562950054084608
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())), reverse=True)
    base = 0
    height = 0
    
    for val in arr:
        if base <= height:
            base += 2**val
        else:
            height += 2**val
    print(base * height)
    print("---------------------")