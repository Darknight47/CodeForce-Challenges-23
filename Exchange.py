"""

--------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1249/B1 ---------------------------------------

The only difference between easy and hard versions is constraints.

There are n kids, each of them is reading a unique book. At the end of any day, the i-th kid will give his book to the pi-th kid (in case of i=pi the kid will give his book to himself). 
It is guaranteed that all values of pi are distinct integers from 1 to n (i.e. p is a permutation). The sequence p doesn't change from day to day, it is fixed.

For example, if n=6 and p=[4,6,1,3,5,2] then at the end of the first day the book of the 1-st kid will belong to the 4-th kid, the 2-nd kid will belong to the 6-th kid and so on. 
At the end of the second day the book of the 1-st kid will belong to the 3-th kid, the 2-nd kid will belong to the 2-th kid and so on.

Your task is to determine the number of the day the book of the i-th child is returned back to him for the first time for every i from 1to n.

Consider the following example: p=[5,1,2,4,3]. The book of the 1-st kid will be passed to the following kids:

after the 1-st day it will belong to the 5-th kid,
after the 2-nd day it will belong to the 3-rd kid,
after the 3-rd day it will belong to the 2-nd kid,after the 4-th day it will belong to the 1-st kid.
So after the fourth day, the book of the first kid will return to its owner. The book of the fourth kid will return to him for the first time after exactly one day.

You have to answer q independent queries.

Input
The first line of the input contains one integer q (1≤q≤200) — the number of queries. Then q queries follow.

The first line of the query contains one integer n (1 ≤ n ≤ 200) — the number of kids in the query. 
The second line of the query contains n integers p1,p2,…,pn (1≤pi≤n, all pi are distinct, i.e. p is a permutation), where pi is the kid which will get the book of the i-th kid.

Output
For each query, print the answer on it: n integers a1,a2,…,an, where ai is the number of the day the book of the i-th child is returned back to him for the first time in this query.

Input:
6
5
1 2 3 4 5
3
2 3 1
6
4 6 2 1 5 3
1
1
4
3 4 1 2
5
5 1 2 4 3

Output:
1 1 1 1 1 
3 3 3 
2 3 3 2 1 3 
1 
2 2 2 2 
4 4 4 1 4 
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    p = [int(x) - 1 for x in input().split()]
    #p = [x - 1 for x in arr]

    ans = [0] * n
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            cycle = []
            current = i

            # Traverse the cycle
            while not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = p[current]

            # The size of the cycle is the answer for EVERY kid in it
            cycle_length = len(cycle)
            for kid in cycle:
                ans[kid] = cycle_length

    print(*ans)
    print("--------------------")