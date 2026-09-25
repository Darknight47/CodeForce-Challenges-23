"""

------------------------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/109/A -----------------------------------------------

Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. 
For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya wonders eagerly what minimum lucky number has the sum of digits equal to n. Help him cope with the task.

Input
The single line contains an integer n (1 ≤ n ≤ 106) — the sum of digits of the required lucky number.

Output
Print on the single line the result — the minimum lucky number, whose sum of digits equals n. If such number does not exist, print -1.

Input:
11

Output:
47
"""
n = int(input())
ans = "-1"
for cnt7 in range(n // 7, -1, -1):
    remainder = n - (7 * cnt7)
    if(remainder % 4 == 0):
        cnt4 = remainder // 4
        ans = "4" * cnt4 + "7" * cnt7
        break
print(ans)