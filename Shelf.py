"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2290/C ------------------------------------

There are n books, and the height of the i-th book is hi. 
You put all the books on a shelf in a row in any order you like.

A book is visible from the left if it is strictly taller than every book to its left. A book is visible from the right if it is strictly taller than every book to its right. 
In particular, the leftmost book is visible from the left, and the rightmost book is visible from the right.

Find the maximum possible number of books that are visible from at least one side, and any arrangement of the books with this number of visible books.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the number of books.

The second line of each test case contains n integers h1,h2,…,hn (1 ≤ hi ≤ 10^9) — the heights of the books.

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print two lines.

In the first line, print a single integer k — the maximum possible number of books that are visible from at least one side.

In the second line, print n integers — the heights of the books from left to right in an arrangement in which exactly k books are visible from at least one side. 
These n integers must be the integers h1,h2,…,hn in some order.

If there are several such arrangements, print any of them.

Input:
5
6
1 2 2 3 3 3
1
5
3
7 7 7
4
4 1 3 2
11
3 1 4 1 5 9 2 6 5 3 5

Output:
5
2 3 3 3 2 1
1
5
2
7 7 7
4
3 4 2 1
10
1 3 4 5 9 5 6 5 3 2 1
"""
def count_visible(arr):
    if not arr:
        return 0
        
    left, right = 0, len(arr) - 1
    max_left = max_right = float('-inf')
    count = 0
    
    while left <= right:
        # Always advance from the side with the smaller current maximum
        if max_left <= max_right:
            if arr[left] > max_left:
                max_left = arr[left]
                count += 1
            left += 1
        else:
            if arr[right] > max_right:
                max_right = arr[right]
                count += 1
            right -= 1
            
    return count

cases = int(input())
for _ in range(cases):
    n = int(input())
    sorted_arr = sorted(list(map(int, input().split())))
    result = [0] * n
    
    left = 0
    right = n - 1
    
    # Place elements alternately from the sorted list into the outer edges of the result
    for i in range(n):
        if i % 2 == 0:
            result[left] = sorted_arr[i]
            left += 1
        else:
            result[right] = sorted_arr[i]
            right -= 1
    count = count_visible(result)
    print(count)
    print(*result)
    print("-----------------")