"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2290/A -------------------------------------

There are three piles of stones. The first pile contains a stones, the second pile contains b stones, and the third pile contains c stones.

You must make exactly one move: take one stone from one of the piles and put it on one of the other two piles. You cannot skip this move, and you cannot make more than one move.

Determine whether you can make this move so that all three piles contain the same number of stones.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤1000). The description of the test cases follows.

The only line of each test case contains three integers a, b, and c (1≤a≤b≤c≤10) — the numbers of stones in the first, second, and third piles.

Output
For each test case, print "YES" if you can make the move so that all three piles contain the same number of stones, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Input:
6
1 2 3
2 2 2
3 4 5
1 1 4
8 9 10
3 5 7

Output:
YES
NO
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    arr = sorted(list(map(int, input().split())))
    # if the difference between them is 1
    if arr[2] - arr[1] == 1 and arr[1] - arr[0] == 1:
        print("YES")
    else:
        print("NO")
    print("----------------")