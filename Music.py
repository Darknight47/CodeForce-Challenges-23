"""

-------------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/507/A ------------------------------------------

Amr is a young coder who likes music a lot. He always wanted to learn how to play music but he was busy coding so he got an idea.

Amr has n instruments, it takes ai days to learn i-th instrument. Being busy, Amr dedicated k days to learn how to play the maximum possible number of instruments.

Amr asked for your help to distribute his free days between instruments so that he can achieve his goal.

Input
The first line contains two numbers n, k (1 ≤ n ≤ 100, 0 ≤ k ≤ 10 000), the number of instruments and number of days respectively.

The second line contains n integers ai (1 ≤ ai ≤ 100), representing number of days required to learn the i-th instrument.

Output
In the first line output one integer m representing the maximum number of instruments Amr can learn.

In the second line output m space-separated integers: the indices of instruments to be learnt. You may output indices in any order.

if there are multiple optimal solutions output any. It is not necessary to use all days for studying.

Input:
4 10
4 3 1 2

Output:
4
1 2 3 4
"""
n, k = map(int, input().split())
indexed_arr = [(int(val), idx) for idx, val in enumerate(input().split())]

indexed_arr.sort()

running_sum = 0
result_indices = []

for val, original_idx in indexed_arr:
    if running_sum + val <= k:
        running_sum += val
        result_indices.append(original_idx + 1)
    else:
        break
print(len(result_indices))
print(*result_indices)