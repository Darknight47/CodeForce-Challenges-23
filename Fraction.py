"""

--------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2278/A --------------------------

You are given two strings p and q, consisting of lowercase English letters.

Interpret the string p as the product of variables written in the numerator of a fraction, and the string q as the product of variables written in the denominator. Each character represents a variable.

Since multiplication is commutative, the variables in both the numerator and the denominator may be reordered arbitrarily. 
In addition, any variable that appears in both the numerator and the denominator may be cancelled. 
Note that a single occurrence of a variable in the denominator can only cancel exactly one occurrence of that variable in the numerator and vice versa.

Determine whether it is possible to simplify the fraction so that the resulting expression is exactly equal to the string six. 
In other words, after performing any number of cancellations and rearrangements, the remaining variables in the numerator must form the string six, and no variables may remain in the denominator.

For example, if p=sinx and q=n, then the variable n can be cancelled, leaving six in the numerator.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The description of each test case follows.

The first line of each test case contains two integers n and m (1 ≤ n, m ≤100) — the lengths of the strings p and q, respectively.

The second line of each test case contains a string p denoting the numerator of the fraction. 
It is guaranteed that the length of the string p is equal to n and that it contains only lowercase English letters.

The third line of each test case contains a string q denoting the denominator of the fraction. It is guaranteed that the length of the string q is equal to m and that it contains only lowercase English letters.

Output
For each test case, print "YES" if you can simplify the fraction so that the resulting expression is exactly equal to the string six and "NO" otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).

Input:
5
4 1
sinx
n
6 7
xixsms
mixsxim
8 5
fixtures
frute
3 3
abc
def
5 10
sixty
codeforces


Output:
YES
NO
YES
NO
NO
"""
from collections import Counter
cases = int(input())
for _ in range(cases):
    p, q = map(int, input().split())
    s1 = input()
    s2 = input()
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    ans1 = "".join((counter1 - counter2).elements())
    ans2 = "".join((counter2 - counter1).elements())
    if(len(ans1) == 3 and ('i' in ans1) and ('s' in ans1) and ('x' in ans1) and len(ans2) == 0):
        print("Yes")
    else:
        print("No")
    print("----------------")