"""


--------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2237/C --------------------------------

Ja the Ghost is playing with rubber ducks again! There are n piles of rubber ducks arranged in a row from left to right. Initially, the i-th pile contains ai rubber ducks.

While the sequence a is not sorted in nondecreasing order, Ja must perform the following operation:

Choose two adjacent piles such that the left pile contains more ducks than the right pile. Ja swaps these two piles, and then adds the number of ducks in the new left pile to the new right pile.
Formally, choose an index i such that 1≤i<n and ai>ai+1. 
Then replace the adjacent pair (ai,ai+1) with (ai+1,ai+ai+1).

For example, if two adjacent piles contain 7 and 3 rubber ducks, then after the operation they contain 3 and 10 rubber ducks.

Ja may choose any index satisfying the condition above at each step. It can be shown that, regardless of his choices, the process eventually ends with the sequence sorted in nondecreasing order.

Ja wants the largest pile at the end of the process to contain as few rubber ducks as possible. Determine the minimum possible value of the largest pile.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains n (1 ≤ n ≤ 2⋅10^5) — the number of piles.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the number of ducks in each pile.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, output a single integer — the minimum possible value of the largest pile.

Input:
10
4
1 2 2 5
2
7 3
3
3 2 1
5
2 2 1 3 3
4
3 1 4 2
5
1 4 3 2 5
6
6 2 5 1 4 3
7
2 7 1 6 3 5 4
8
8 1 7 2 6 3 5 4
5
1000000000 999999999 999999998 999999997 999999996

Output:
5
10
6
3
6
14
21
26
36
4999999990
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        first = arr[i]
        second = arr[i + 1]
        if(second < first):
            arr[i + 1] = second + first
    print(arr[-1])
    print("-----------------")