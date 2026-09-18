"""

---------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1770/A ---------------------------

Kiyora has n whiteboards numbered from 1 to n. Initially, the i-th whiteboard has the integer ai written on it.

Koxia performs m operations. The j-th operation is to choose one of the whiteboards and change the integer written on it to bj.

Find the maximum possible sum of integers written on the whiteboards after performing all m operations.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. The description of test cases follows.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤ 100).

The second line of each test case contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9).

The third line of each test case contains m integers b1,b2,…,bm (1 ≤ bi ≤ 10^9).

Output
For each test case, output a single integer — the maximum possible sum of integers written on whiteboards after performing all m operations.

Input:
4
3 2
1 2 3
4 5
2 3
1 2
3 4 5
1 1
100
1
5 3
1 1 1 1 1
1000000000 1000000000 1000000000

Output:
12
9
1
3000000002
"""
cases = int(input())
for _ in range(cases):
  n, m = map(int, input().split())
 
  arr = list(map(int, input().split()))
  brr = list(map(int, input().split()))
  
 
  for num in brr:
    arr.sort()
    arr[0] = num
 
  print(sum(arr))