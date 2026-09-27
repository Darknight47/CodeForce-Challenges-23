"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/560/A ----------------------

A magic island Geraldion, where Gerald lives, has its own currency system. It uses banknotes of several values. 
But the problem is, the system is not perfect and sometimes it happens that Geraldionians cannot express a certain sum of 
money with any set of banknotes. Of course, they can use any number of banknotes of each value. Such sum is called unfortunate. 
Gerald wondered: what is the minimum unfortunate sum?

Input
The first line contains number n (1 ≤ n ≤ 1000) — the number of values of the banknotes that used in Geraldion.

The second line contains n distinct space-separated numbers a1, a2, ..., an (1 ≤ ai ≤ 106) — the values of the banknotes.

Output
Print a single line — the minimum unfortunate sum. If there are no unfortunate sums, print  - 1.

Input:
5
1 2 3 4 5


Output:
-1
"""
n = int(input())
arr = sorted(list(map(int, input().split())))
if(arr[0] == 1):
    print(-1)
else:
    print(1)
