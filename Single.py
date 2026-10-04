"""

------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1253/A ---------------------

You're given two arrays a[1…n] and b[1…n], both of the same length n.

In order to perform a push operation, you have to choose three integers l,r,k 
satisfying 1 ≤ l ≤ r ≤ n and k > 0. Then, you will add k to elements al,al+1,…,ar.

For example, if a=[3,7,1,4,1,2] and you choose (l=3,r=5,k=2), the array a will become [3,7,3,6,3––––––,2].

You can do this operation at most once. Can you make array a equal to array b?

(We consider that a=b if and only if, for every 1≤i≤n, ai=bi)

Input
The first line contains a single integer t (1 ≤ t ≤ 20) — the number of test cases in the input.

The first line of each test case contains a single integer n (1≤n≤100 000) — the number of elements in each array.

The second line of each test case contains n integers a1,a2,…,an (1≤ai≤1000).

The third line of each test case contains n integers b1,b2,…,bn (1 ≤ bi ≤ 1000).

It is guaranteed that the sum of n over all test cases doesn't exceed 10^5.

Output
For each test case, output one line containing "YES" if it's possible to make arrays a and b equal by performing 
at most once the described operation or "NO" if it's impossible.

You can print each letter in any case (upper or lower).

Input:
4
6
3 7 1 4 1 2
3 7 3 6 3 2
5
1 1 1 1 1
1 2 1 3 1
2
42 42
42 42
1
7
6


Output:
YES
NO
YES
NO
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    ok = True
    first_range_completed = False
    first_time = True
    for i in range(n):
        first = arr[i]
        second = brr[i]
        if(first > second):
            ok = False
            break
        if(first < second and not first_range_completed):
            temp = second - first
            if(first_time):
                first_time = False
                total_temp = temp
            else:
                if(temp != total_temp):
                    ok = False
                    break
        elif(first == second and not first_time):
            first_range_completed = True
        elif(first < second and first_range_completed):
            ok = False
            break
    print("YES" if ok else "NO")
    print("---------------------")