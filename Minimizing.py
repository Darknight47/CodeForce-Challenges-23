"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1230/B ---------------------

Ania has a large integer S. 
Its decimal representation has length n and doesn't contain any leading zeroes. 
Ania is allowed to change at most k digits of S. 
She wants to do it in such a way that S still won't contain any leading zeroes and it'll be minimal possible. 
What integer will Ania finish with?

Input
The first line contains two integers n and k (1≤n≤200000, 0≤k≤n) — the number of digits in the decimal representation of S and the maximum allowed number of changed digits.

The second line contains the integer S. It's guaranteed that S has exactly n digits and doesn't contain any leading zeroes.

Output
Output the minimal possible value of S which Ania can end with. Note that the resulting integer should also have n digits.

Input:
5 3
51528

Output:
10028
"""
n, k = map(int, input().split())
s = list(input())
if(k == 0):
    print("".join(s))
else:
    if(n < 2):
        print(0)
    else:    
        if(s[0] != '1'):
            s[0] = '1'
            k -= 1
        for i in range(1, n):
            if(k <= 0):
                break
            if(s[i] != '0'):
                s[i] = '0'
                k -= 1
        print("".join(s))