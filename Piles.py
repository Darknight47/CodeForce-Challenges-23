"""

------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2266/B ---------------------------------------

Alice and Bob are playing a game with three piles of stones. Initially, Alice has a stones, Bob has b stones, and the third pile contains c stones.

Alice and Bob take turns, with Alice going first. On each turn, the current player may take any number of stones from the third pile, possibly zero, and add them to their own pile.

If both players take zero stones on two consecutive turns, the game ends.

Let A and B be the final numbers of stones Alice and Bob have, respectively. The score of the game is |A−B|.

Alice wants to maximize the score, while Bob wants to minimize it. Assuming both players play optimally, find the final score.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case contains three integers a, b, and c (0≤a,b,c≤10^9) — the initial numbers of stones Alice has, Bob has, and the third pile has, respectively.

Output
For each test case, output one integer — the final score if both players play optimally.

It is important to use a 64-bit integer type, such as long long in C++.

Input:
5
3 6 3
3 6 10
5 5 4
2 5 6
67676767 41414141 998244353

Output:
3
7
4
3
1024506979
"""
cases = int(input())
for _ in range(cases):
    a, b, c = map(int, input().split())
    diff1 = abs(a - b)
    diff2 = abs( (a + c) - b )
    print(max(diff1, diff2))
    print("----------------")