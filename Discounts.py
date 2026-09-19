"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/2143/B -----------------------------------------

You want to buy n products with prices a1,a2,…,an. You can either:

buy product i individually, paying ai coins, or
use a discount voucher to buy it as part of a group purchase.
You have k discount vouchers with values b1,b2,…,bk. A voucher of value x allows you to select exactly x products and pay only for the x−1 most expensive ones, 
as such, you can consider that the cheapest product in the group is free. Each product can be included in at most one discount group, even if it is not the free one. 
Also, any single voucher can be used at most one single time.

What is the minimum total cost required to purchase all n products?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The first line contains two integers n and k (1 ≤ n, k ≤ 2⋅10^5) —the number of products and the number of available discount vouchers.

The second line contains n integers a1,a2,…,an (1 ≤ ai ≤ 10^9) — the prices of the products.

The third line contains k integers b1,b2,…,bk (1≤bi≤n) — the values of the discount vouchers.

It is guaranteed that the sum of n across all test cases does not exceed 2⋅10^5, and the sum of k across all test cases does not exceed 2⋅10^5.

Output
Print t lines. The i-th line should contain the answer for the i-th test case — the minimum total cost required to purchase all products in that test case.

Input:
5
5 3
18 3 7 2 9
3 1 1
6 1
1 2 6 3 3 4
5
2 3
1 1
2 2 2
1 1
10
1
5 3
99 99 999 999 123
2 1 4

Output:
10
17
1
0
1197
"""
cases = int(input())
for _ in range(cases):
    n, k = map(int, input().split())
    arr = sorted(list(map(int, input().split())), reverse= True)
    brr = sorted(list(map(int, input().split())))
    current_index = 0
    
    for size in brr:
        # If we have already reached or exceeded the end of arr, stop
        elements_left = n - current_index
        
        # If size is bigger than elements left, break the loop
        if size > elements_left:
            break
        if current_index >= n:
            break
            
        # If the size goes out of bounds, we take what's left (arr_len - 1)
        target_index = min(current_index + size - 1, n - 1)
        
        arr[target_index] = 0
        
        current_index += size
        
    print(sum(arr))
    print("--------------------")