"""

-------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2275/B -------------------------

Recently, K1o0n bought himself a new expensive printer, which is distinguished by its memory, that is, it may not print immediately. 
Yesterday, while he was away from his new purchase, his friends used the printer.

There are n documents numbered from 1 to n. 
Initially, the printer memory is empty. The friends sequentially performed n commands on the printer, where the i-th command can be one of:

'1'  — scanning. Document i is sent to the device memory and is placed on top of everything already there.
'2'  — printing from memory. If the memory is not empty, the device prints the topmost document in memory and removes it from there. Otherwise, the device prints document i.
'3'  — quick print. The device prints document i.
Today, the friends came to K1o0n with a complaint — not all documents were printed. Help K1o0n find the indices of all documents that were not printed.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) — the number of testcases.

The first line of each testcase contains an integer n (1 ≤ n ≤ 2⋅10^5) — the number of documents.

The second line of each testcase contains a string s of length n, consisting of the characters '1', '2' and '3' — the friends' commands.

It is guaranteed that the sum of n over all testcases does not exceed 2⋅10^5.

Output
For each testcase, output two lines.

In the first line — the number k of documents that were not printed.

In the second line — their numbers in increasing order, separated by spaces. If k=0, the second line is empty.

Input:
6
2
12
2
13
2
23
6
112332
3
112
6
211213

Output:
1
2 
1
1 
0


2
3 6 
2
1 3 
3
2 4 5 
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    s = input()
    ones_stack = []
    survived_twos = []

    for index, char in enumerate(s, start=1):
        if(char == '1'):
            ones_stack.append(index)
        elif(char == '2'):
            if(ones_stack):
                ones_stack.pop()
                survived_twos.append(index)
            else:
                pass
    ans = sorted(survived_twos + ones_stack)
    print(len(ans))
    print(*ans)