"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1784/A ------------------------------

This is the easy version of the problem. In this version, you only need to find the answer once. In this version, hacks are not allowed.

In a computer game, you are fighting against n monsters. Monster number i has ai health points, all ai are integers. A monster is alive while it has at least 1 health point.

You can cast spells of two types:

Deal 1 damage to any single alive monster of your choice.
Deal 1 damage to all alive monsters. If at least one monster dies (ends up with 0 health points) as a result of this action, then repeat it (and keep repeating while at least one monster dies every time).
Dealing 1 damage to a monster reduces its health by 1.

Spells of type 1 can be cast any number of times, while a spell of type 2 can be cast at most once during the game.

What is the smallest number of times you need to cast spells of type 1 to kill all monsters?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

Each test case consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of monsters.

The second line contains n integers a1,a2,…,an (1≤ai≤n) — monsters' health points.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print a single integer — the smallest number of times you need to cast spells of type 1 to kill all monsters.

Input:
2
3
3 1 2
6
4 1 5 4 1 1

Output:
0
4
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    
    # We track the current target we are trying to fill, starting at 1.
    current_target = 1
    total_ops = 0
    
    for num in arr:
        if num >= current_target:
            total_ops += (num - current_target)
            current_target += 1
            
    print(total_ops)