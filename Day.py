"""

---------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1199/A ------------------------------

For years, the Day of city N was held in the most rainy day of summer. 
New mayor decided to break this tradition and select a not-so-rainy day for the celebration. 
The mayor knows the weather forecast for the n days of summer. On the i-th day, ai millimeters of rain will fall. All values ai are distinct.

The mayor knows that citizens will watch the weather x days before the celebration and y days after. 
Because of that, he says that a day d is not-so-rainy if ad is smaller than rain amounts at each of x days before day d and and each of y days after day d. 
In other words, ad<aj should hold for all d−x≤j<d and d<j≤d+y. Citizens only watch the weather during summer, so we only consider such j that 1≤j≤n.

Help mayor find the earliest not-so-rainy day of summer.

Input
The first line contains three integers n, x and y (1≤n≤100000, 0≤x,y≤7) — the number of days in summer, the number of days citizens watch the weather before the celebration and the number of days they do that after.

The second line contains n distinct integers a1, a2, ..., an (1 ≤ ai ≤ 10^9), where ai denotes the rain amount on the i-th day.

Output
Print a single integer — the index of the earliest not-so-rainy day of summer. We can show that the answer always exists.

Input:
10 2 2
10 9 6 7 8 3 2 1 4 5

Output:
3
"""
n, x, y = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    current_element = arr[i]   
    found_smaller_left = False
    for step in range(1, x + 1):
        target_idx = i - step
        
        if target_idx < 0:
            break
        
        if arr[target_idx] < current_element:
            found_smaller_left = True
            break
            
    found_smaller_right = False
    for step in range(1, y + 1):
        target_idx = i + step
        if target_idx >= n:
            break
        if arr[target_idx] < current_element:
            found_smaller_right = True
            break
        
    if not found_smaller_left and not found_smaller_right:
        ans = i
        break
        
print(ans + 1)