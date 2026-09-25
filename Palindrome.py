"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2267/A -------------------------------------


Ali has a string s consisting of n lowercase Latin letters. He also has a character c, which is a lowercase Latin letter. In one coin, he can perform the following operation on the string s:

First, he chooses an index 1≤i≤n.
Then he replaces si with the character c.
Ali wants to turn the string s into a palindrome∗, but he does not want to spend too many coins on it. 
Your task — compute the minimum number of coins he has to spend to turn the string s into a palindrome.

∗ A string t of length m is a palindrome if ti=tm−i+1 holds for every 1≤i≤m

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤500). The description of the test cases follows.

The first line of each test case contains an integer n and a lowercase Latin letter c (1≤n≤100) — the length of the string s and the character c.

The second line of each test case contains the string s consisting of n lowercase Latin letters.

Output
For each test case, output one number — the minimum number of coins Ali needs to spend for the string to become a palindrome.

Input:
5
4 b
abca
3 p
xyx
5 e
abcbb
8 d
adbccbad
10 c
codeforces

Output:
1
0
2
2
8
"""
cases = int(input())
for _ in range(cases):
    sze, chr = input().split()
    sze = int(sze)
    s = input()
    left = 0
    right = sze - 1
    ans = 0

    while left < right:
        if(s[left] != s[right]):
            if(s[left] == chr or s[right] == chr):
                ans += 1
            else:
                ans += 2
        left += 1
        right -= 1
    print(ans)
    print("------------------")