"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1117/B --------------------------------

There are n emotes in very popular digital collectible card game (the game is pretty famous so we won't say its name). 
The i-th emote increases the opponent's happiness by ai units (we all know that emotes in this game are used to make opponents happy).

You have time to use some emotes only m times. You are allowed to use any emotion once, more than once, or not use it at all. 
The only restriction is that you cannot use the same emote more than k times in a row (otherwise the opponent will think that you're trolling him).

Note that two emotes i and j (i≠j) such that ai=aj are considered different.

You have to make your opponent as happy as possible. Find the maximum possible opponent's happiness.

Input
The first line of the input contains three integers n,m and k (2 ≤ n ≤ 2⋅10^5, 1 ≤ k ≤ m ≤ 2⋅10^9) — the number of emotes, the number of times you can use emotes and the maximum number of times you may use the same emote in a row.

The second line of the input contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9), where ai is value of the happiness of the i-th emote.

Output
Print one integer — the maximum opponent's happiness if you use emotes in a way satisfying the problem statement.

Input:
6 9 2
1 3 3 7 4 2

Output:
54
"""
n, m, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))
top1 = arr[-1]
top2 = arr[-2]
# sum of m-repeats, top1 is repeated k times, top2 comes up once, then top1 is repeated k times again, so on until m is reached
total_sum = (m // (k + 1)) * (top1 * k + top2) + (m % (k + 1)) * top1
print(total_sum)