"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/334/A ------------------------------------------

Gerald has n younger brothers and their number happens to be even. One day he bought n2 candy bags. 
One bag has one candy, one bag has two candies, one bag has three candies and so on. In fact, for each integer k from 1 to n2 he has exactly one bag with k candies.

Help him give n bags of candies to each brother so that all brothers got the same number of candies.

Input
The single line contains a single integer n (n is even, 2 ≤ n ≤ 100) — the number of Gerald's brothers.

Output
Let's assume that Gerald indexes his brothers with numbers from 1 to n. 
You need to print n lines, on the i-th line print n integers — the numbers of candies in the bags for the i-th brother. 
Naturally, all these numbers should be distinct and be within limits from 1 to n2. You can print the numbers in the lines in any order.

It is guaranteed that the solution exists at the given limits.

Input:
2

Output:
1 4
2 3
"""
import sys
from itertools import chain
n = int(input())
k = n // 2
n_squared = n * n
output = []

for i in range(n):
    left_start = 1 + i * k
    right_start = n_squared - (i + 1) * k + 1
    
    r1 = range(left_start, left_start + k)
    r2 = range(right_start, right_start + k)
    sys.stdout.write(" ".join(map(str, chain(r1, r2))) + "\n")