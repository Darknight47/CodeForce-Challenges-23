"""

-------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1266/A ---------------------------------

Bob is a competitive programmer. He wants to become red, and for that he needs a strict training regime. 
He went to the annual meeting of grandmasters and asked n of them how much effort they needed to reach red.

"Oh, I just spent xi hours solving problems", said the i-th of them.

Bob wants to train his math skills, so for each answer he wrote down the number of minutes (60⋅xi), 
thanked the grandmasters and went home. Bob could write numbers with leading zeroes — for example, if some grandmaster answered that he had spent 2 hours, Bob could write 000120 instead of 120.

Alice wanted to tease Bob and so she took the numbers Bob wrote down, and for each of them she did one of the following independently:

rearranged its digits, or
wrote a random number. This way, Alice generated n numbers, denoted y1, ..., yn.

For each of the numbers, help Bob determine whether yi can be a permutation of a number divisible by 60 (possibly with leading zeroes).

Input
The first line contains a single integer n (1 ≤ n ≤ 418) — the number of grandmasters Bob asked.

Then n lines follow, the i-th of which contains a single integer yi — the number that Alice wrote down.

Each of these numbers has between 2 and 100 digits '0' through '9'. They can contain leading zeroes.

Output
Output n lines.

For each i, output the following. 
If it is possible to rearrange the digits of yi such that the resulting number is divisible by 60, output "red" (quotes for clarity). Otherwise, output "cyan".


Input:
6
603
006
205
228
1053
0000000000000000000000000000000000000000000000

Output:
red
red
cyan
cyan
cyan
red
"""
cases = int(input())
for _ in range(cases):
    num_str = input()
    total_sum = 0
    evens = "02468"
    even = 0
    zero = False
    for dig in num_str:
        digit = int(dig)
        total_sum += digit
        if(dig in evens):
            even += 1
        if(dig == '0'):
            zero = True
    ok = False
    if(total_sum % 3 == 0 and even >= 2 and zero):
        ok = True
    print("red" if ok else "cyan")
    print("-----------------")