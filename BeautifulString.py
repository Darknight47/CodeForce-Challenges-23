"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1265/A ------------------------------------

A string is called beautiful if no two consecutive characters are equal. For example, "ababcb", "a" and "abab" are beautiful strings, while "aaaaaa", "abaa" and "bb" are not.

Ahcl wants to construct a beautiful string. He has a string s, consisting of only characters 'a', 'b', 'c' and '?'. 
Ahcl needs to replace each character '?' with one of the three characters 'a', 'b' or 'c', such that the resulting string is beautiful. Please help him!

More formally, after replacing all characters '?', the condition si≠si+1 should be satisfied for all 1≤i≤|s|−1, where |s| is the length of the string s.

Input
The first line contains positive integer t (1 ≤ t ≤ 1000) — the number of test cases. Next t lines contain the descriptions of test cases.

Each line contains a non-empty string s consisting of only characters 'a', 'b', 'c' and '?'.

It is guaranteed that in each test case a string s has at least one character '?'. The sum of lengths of strings s in all test cases does not exceed 10^5.

Output
For each test case given in the input print the answer in the following format:

If it is impossible to create a beautiful string, print "-1" (without quotes);
Otherwise, print the resulting beautiful string after replacing all '?' characters. If there are multiple answers, you can print any of them.

Input:
3
a???cb
a??bbc
a?b?c

Output:
ababcb
-1
acbac
"""
cases = int(input())
for _ in range(cases):
    s = input()
    chars = list(s)
    n = len(chars)
    ok = True
    for i in range(n):
        if chars[i] == '?':
            left = chars[i - 1] if i > 0 else None
            right = chars[i + 1] if i < n - 1 else None
           
            for option in ['a', 'b', 'c']:
                if option != left and option != right:
                    chars[i] = option
                    break 
        else:
            if i < n - 1 and chars[i] == chars[i + 1]:
                ok = False
                break                    
    if ok:
        print("".join(chars))    
    else:
        print(-1)