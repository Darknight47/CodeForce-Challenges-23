"""

-------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1859/B -------------------------------

Artem suggested a game to the girl Olya. There is a list of n arrays, where the i-th array contains mi≥2 positive integers ai,1,ai,2,…,ai,mi.

Olya can move at most one (possibly 0) integer from each array to another array. Note that integers can be moved from one array only once, 
but integers can be added to one array multiple times, and all the movements are done at the same time.

The beauty of the list of arrays is defined as the sum ∑ni=1minmij=1ai,j. 
In other words, for each array, we find the minimum value in it and then sum up these values.

The goal of the game is to maximize the beauty of the list of arrays. Help Olya win this challenging game!

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 25000) — the number of test cases. The description of test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 25000) — the number of arrays in the list.

This is followed by descriptions of the arrays. Each array description consists of two lines.

The first line contains a single integer mi (2 ≤ mi ≤ 50000) — the number of elements in the i-th array.

The next line contains mi integers ai,1,ai,2,…,ai,mi (1 ≤ ai, j ≤10^9) — the elements of the i-th array.

It is guaranteed that the sum of mi over all test cases does not exceed 50000.

Output
For each test case, output a single line containing a single integer — the maximum beauty of the list of arrays that Olya can achieve.

Input:
3
2
2
1 2
2
4 3
1
3
100 1 6
3
4
1001 7 1007 5
3
8 11 6
2
2 9

Output:
5
1
19
"""
cases = int(input())
for _ in range(cases):
    arrs = int(input())
    two_elements_arrs = []
    
    for _ in range(arrs):
        tmp_sze = int(input())
        v = list(map(int, input().split()))
        
        # Find the first minimum
        minel = min(v)
        two_elements_arrs.append(minel)
        
        v.remove(minel)
        
        # Find the second minimum from the remaining elements
        second_min = min(v)
        two_elements_arrs.append(second_min)

    global_min = float('inf')
    sum_max_elements = 0
    smallest_max = float('inf')
    
    for i in range(0, len(two_elements_arrs), 2):
        val1 = two_elements_arrs[i]
        val2 = two_elements_arrs[i+1]
        
        if val1 < global_min: global_min = val1
        if val2 < global_min: global_min = val2
        
        pair_max = val1 if val1 > val2 else val2
        sum_max_elements += pair_max
        if pair_max < smallest_max:
            smallest_max = pair_max
    
    print(global_min + sum_max_elements - smallest_max)
    print("-------------------")