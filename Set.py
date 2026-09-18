"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2029/A ------------------------------

You are given a positive integer k and a set S of all integers from l to r (inclusive).

You can perform the following two-step operation any number of times (possibly zero):

First, choose a number x from the set S, such that there are at least k multiples of x in S (including x itself);
Then, remove x from S (note that nothing else is removed).
Find the maximum possible number of operations that can be performed.

Input
Each test contains multiple test cases. The first line of the input contains a single integer t (1≤t≤10^4) — the number of test cases. The description of test cases follows.

The only line of each test case contains three integers l, r, and k (1≤l≤r≤10^9, 1≤k≤r−l+1) — the minimum integer in S, the maximum integer in S, and the parameter k.

Output
For each test case, output a single integer — the maximum possible number of operations that can be performed.

Input:
8
3 9 2
4 9 1
7 9 2
2 10 2
154 220 2
147 294 2
998 24435 3
1 1000000000 2

Output:
2
6
0
4
0
1
7148
500000000
"""
cases = int(input())
for _ in range(cases):
    l, r, x = map(int, input().split())
    upper_bound = r // x
    ans = max(0, upper_bound - l + 1)
    print(ans)
    print("-----------------")