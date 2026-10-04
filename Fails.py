"""

--------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1174/A -----------------

You're given an array a of length 2n. 
Is it possible to reorder it in such way so that the sum of the first n elements isn't equal to the sum of the last n elements?

Input
The first line contains an integer n (1 ≤ n ≤ 1000), where 2n is the number of elements in the array a.

The second line contains 2n space-separated integers a1, a2, …, a2n (1 ≤ ai ≤ 10^6) — the elements of the array a.

Output
If there's no solution, print "-1" (without quotes). 
Otherwise, print a single line containing 2n space-separated integers. They must form a reordering of a. 
You are allowed to not change the order.

Input:
3
1 2 2 1 3 1

Output:
2 1 3 1 1 2
"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
first = sum(arr[:n])
second = sum(arr[n:])
if(first == second):
    print(-1)
else:
    print(*arr)