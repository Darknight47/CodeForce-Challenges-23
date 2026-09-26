"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2267/B --------------------------------

The mode of an array — is the number that appears the maximum number of times in the array. 
If several numbers appear the maximum number of times, the mode is the largest among them. 
For example, the mode of the array [1,1,2] is 1, and the mode of the array [3,4] is 4.

You are given an array a consisting of n integers. You may arbitrarily permute the numbers in array a in any order. 
Your task — is to rearrange the numbers in array a so that the sum of the modes over all prefixes of the array is maximized.

For example, the array [2,3,2] can be rearranged as [3,2,2]. Then the sum of the modes over all prefixes is determined as follows:

The prefix of length 1 is [3]. The mode of this prefix is 3.
The prefix of length 2 is [3,2]. The mode of this prefix is 3.
The prefix of length 3 is [3,2,2]. The mode of this prefix is 2.
Thus, the sum of the modes is 3+3+2=8. It can be proven that for this arrangement of array a, the answer is maximal.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 500). The description of the test cases follows.

The first line of each test case contains one integer n (1 ≤ n ≤ 100) — the size of the array.

The second line of each test case contains n integers a1,a2,…an (1≤ai≤100) — the elements of the array.

Output
For each test case, output a new array whose sum of the modes over all prefixes is maximal. If there are several optimal answers, output any of them.

Input:
7
3
2 3 2
6
4 4 2 1 3 1
5
1 3 2 4 2
4
1 1 1 2
7
1 2 3 4 5 6 7
8
1 1 4 2 3 3 3 2
8
4 3 3 3 2 1 4 1

Output:
3 2 2
4 4 3 2 1 1
4 1 3 2 2
2 1 1 1
7 1 2 3 4 5 6
4 3 2 1 3 3 1 2
4 4 3 3 2 1 1 3
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    counts = Counter(arr)
    sorted_keys = sorted(counts.keys(), reverse=True)
    result = []
    
    while +counts:  # '+counts' removes keys with 0 or negative counts
        for key in sorted_keys:
            if counts[key] > 0:
                result.append(key)
                counts[key] -= 1
                
    print(*result)
    print("---------------")