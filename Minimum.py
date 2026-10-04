"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1101/A ----------------

You are given q queries in the following form:

Given three integers li, ri and di, find minimum positive integer xi such that it is divisible by di and it does not belong to the segment [li,ri].

Can you answer all the queries?

Recall that a number x belongs to segment [l,r] if l≤x≤r.

Input
The first line contains one integer q (1 ≤ q ≤ 500) — the number of queries.

Then q lines follow, each containing a query given in the format li ri di (1 ≤ li ≤ ri ≤ 10^9, 1 ≤ di ≤ 10^9). li, ri and di are integers.

Output
For each query print one integer: the answer to this query.

Input:
5
2 4 2
5 10 4
3 10 1
1 2 3
4 6 5

Output:
6
4
1
3
10
"""
cases = int(input())
for _ in range(cases):
    l, r, d = map(int, input().split())
    if(d < l or d > r):
        print(d)
    else:
        print((r // d + 1) * d)