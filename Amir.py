"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/804/A ------------------------

A few years ago Sajjad left his school and register to another one due to security reasons. Now he wishes to find Amir, one of his schoolmates and good friends.

There are n schools numerated from 1 to n. One can travel between each pair of them, to do so, he needs to buy a ticket. 
The ticker between schools i and j costs  and can be used multiple times. Help Sajjad to find the minimum cost he needs to pay for tickets to visit all schools. He can start and finish in any school.

Input
The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of schools.

Output
Print single integer: the minimum cost of tickets needed to visit all schools.

Input:
2

Output:
0
"""
n = int(input())
if(n % 2 == 0):
    ans = (n // 2) - 1
else:
    ans = n//2
print(ans)