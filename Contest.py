"""

---------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2266/A --------------------------------

The next programming contest has three problems and n participants.

Problem 1 is easy, problem 2 is medium, and problem 3 is hard.

A participant is called weak if they did not solve all three problems.

Unfortunately, the scoreboard was lost. The only remaining information is an array a of length 3, where ai is the number of participants who solved problem i.

Among all scoreboards consistent with this information, find the minimum possible number of weak participants.

Input
The first line contains an integer t (1≤t≤3000) — the number of test cases.

The first line of each test case contains an integer n (1≤n≤9) — the number of participants.

The second line of each test case contains three integers a1,a2,a3 (0≤ai≤n), where ai is the number of participants who solved problem i.

Output
For each test case, print a single integer — the minimum possible number of weak participants.

Input:
6
3
3 3 3
4
4 4 3
1
1 1 1
9
9 8 9
5
0 5 5
6
4 3 2

Output:
0
1
0
1
5
4
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = n - min(arr)
    print(ans)
    print("----------------")