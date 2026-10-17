"""

----------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1419/D1 ----------------------------------

This is the easy version of the problem. The difference between the versions is that in the easy version all prices ai are different. 
You can make hacks if and only if you solved both versions of the problem.

Today is Sage's birthday, and she will go shopping to buy ice spheres. All n ice spheres are placed in a row and they are numbered from 1 to n from left to right. 
Each ice sphere has a positive integer price. In this version all prices are different.

An ice sphere is cheap if it costs strictly less than two neighboring ice spheres: the nearest to the left and the nearest to the right. 
The leftmost and the rightmost ice spheres are not cheap. Sage will choose all cheap ice spheres and then buy only them.

You can visit the shop before Sage and reorder the ice spheres as you wish. Find out the maximum number of ice spheres that Sage can buy, and show how the ice spheres should be reordered.

Input
The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of ice spheres in the shop.

The second line contains n different integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the prices of ice spheres.

Output
In the first line print the maximum number of ice spheres that Sage can buy.

In the second line print the prices of ice spheres in the optimal order. If there are several correct answers, you can print any of them.

Input:
5
1 2 3 4 5

Output:
2
3 1 4 2 5 
"""
n = int(input())
arr = sorted(list(map(int, input().split())))

ans = [0] * n
left_idx = 0
right_idx = n - 1
mid_elems = 0

for i in range(n - 1, -1, -1):
    step_from_right = (n - 1) - i
    if(step_from_right % 2 == 0):
        ans[i] = arr[right_idx]
        right_idx -= 1
    else:
        ans[i] = arr[left_idx]
        left_idx += 1

    check_idx = i + 1
    if(0 < check_idx < n - 1):
        if(ans[check_idx] < ans[check_idx - 1] and ans[check_idx] < ans[check_idx + 1]):
            mid_elems += 1
print(mid_elems)
print(*ans)