"""

--------------------------------- Link for the chllenge: https://codeforces.com/problemset/problem/727/A --------------------

Vasily has a number a, which he wants to turn into a number b. For this purpose, he can do two types of operations:

multiply the current number by 2 (that is, replace the number x by 2·x);
append the digit 1 to the right of current number (that is, replace the number x by 10·x + 1).
You need to help Vasily to transform the number a into the number b using only the operations described above, 
or find that it is impossible.

Note that in this task you are not required to minimize the number of operations. It suffices to find any way to transform a into b.

Input
The first line contains two positive integers a and b (1 ≤ a < b ≤ 10^9) — 
the number which Vasily has and the number he wants to have.

Output
If there is no way to get b from a, print "NO" (without quotes).

Otherwise print three lines. On the first line print "YES" (without quotes). 
The second line should contain single integer k — the length of the transformation sequence. 
On the third line print the sequence of transformations x1, x2, ..., xk, where:

x1 should be equal to a,
xk should be equal to b,
xi should be obtained from xi - 1 using any of two described operations (1 < i ≤ k).
If there are multiple answers, print any of them.

Input:
2 162

Output:
YES
5
2 4 8 81 162 
"""
a, b = map(int, input().split())

possible = False
nums = [b]

while b >= a: 
    if b == a:
        possible = True
        break

    if b % 2 == 0:
        b //= 2
    # Only allow odd numbers that explicitly end in 1
    elif b % 10 == 1: 
        b //= 10  
    else:
        # Ends in 3, 5, 7, or 9 -> mathematically impossible
        break 
        
    nums.append(b)

print("YES" if possible else "NO")
if possible:
    print(len(nums))
    nums.reverse()
    print(*nums)