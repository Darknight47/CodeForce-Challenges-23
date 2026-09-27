"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1139/B ---------------------

You went to the store, selling n types of chocolates. There are ai chocolates of type i in stock.

You have unlimited amount of cash (so you are not restricted by any prices) and want to buy as many chocolates as possible. 
However if you buy xi chocolates of type i (clearly, 0≤xi≤ai), then for all 1≤j<i at least one of the following must hold:

xj=0 (you bought zero chocolates of type j)
xj<xi (you bought less chocolates of type j than of type i)
For example, the array x=[0,0,1,2,10] satisfies the requirement above (assuming that all ai≥xi), while arrays x=[0,1,0], x=[5,5] and x=[3,2] don't.

Calculate the maximum number of chocolates you can buy.

Input
The first line contains an integer n (1 ≤ n ≤ 2⋅10^5), denoting the number of types of chocolate.

The next line contains n integers ai (1 ≤ ai ≤ 10^9), denoting the number of chocolates of each type.

Output
Print the maximum number of chocolates you can buy.

Input:
5
1 2 1 3 6

Output:
10
"""
sze = int(input())
arr = list(map(int, input().split()))
ans = 0
full = True
for i in range(sze - 1, 0, -1):
    first = arr[i]
    second = arr[i - 1]
    if(first <= 0):
        full = False
        break
    if(first <= second):
        arr[i - 1] = first - 1
    ans += first
if(full):
    ans += arr[0]
print(ans)
print("----------------------")