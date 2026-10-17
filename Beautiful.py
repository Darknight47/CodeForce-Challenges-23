"""

----------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1841/B ---------------------------------

The array [a1,a2,…,ak] is called beautiful if it is possible to remove several (maybe zero) elements from the beginning of the array and insert all these 
elements to the back of the array in the same order in such a way that the resulting array is sorted in non-descending order.

In other words, the array [a1,a2,…,ak] is beautiful if there exists an integer i∈[0,k−1] such that the array [ai+1,ai+2,…,ak−1,ak,a1,a2,…,ai] is sorted in non-descending order.

For example:

[3,7,7,9,2,3] is beautiful: we can remove four first elements and insert them to the back in the same order, and we get the array [2,3,3,7,7,9], which is sorted in non-descending order;
[1,2,3,4,5] is beautiful: we can remove zero first elements and insert them to the back, and we get the array [1,2,3,4,5], which is sorted in non-descending order;
[5,2,2,1] is not beautiful.
Note that any array consisting of zero elements or one element is beautiful.

You are given an array a, which is initially empty. You have to process q queries to it. 
During the i-th query, you will be given one integer xi, and you have to do the following:

if you can append the integer xi to the back of the array a so that the array a stays beautiful, you have to append it;
otherwise, do nothing.
After each query, report whether you appended the given integer xi, or not.

Input
The first line contains one integer t (1 ≤ t ≤ 10^4) — the number of test cases.

Each test case consists of two lines. The first line contains one integer q (1 ≤ q ≤ 2⋅10^5) — the number of queries. 
The second line contains q integers x1,x2,…,xq (0 ≤ xi ≤ 10^9).

Additional constraint on the input: the sum of q over all test cases does not exceed 2⋅10^5).

Output
For each test case, print one string consisting of exactly q characters. 
The i-th character of the string should be 1 if you appended the integer during the i-th query; otherwise, it should be 0.

Input:
3
9
3 7 7 9 2 4 6 3 4
5
1 1 1 1 1
5
3 2 1 2 3

Output:
111110010
11111
11011
"""
cases = int(input())
for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ["1"]

    first_val = arr[0]
    last_valid_val = arr[0]
    has_decreased = False

    for i in range(1, n):
        curr = arr[i]

        if(not has_decreased):
            if(curr >= last_valid_val):
                ans.append('1')
                last_valid_val = curr
            elif(curr <= first_val):
                ans.append('1')
                has_decreased = True
                last_valid_val = curr
            else:
                ans.append('0')
        else:
            if(curr >= last_valid_val and curr <= first_val):
                ans.append('1')
                last_valid_val = curr
            else:
                ans.append('0')
    print("".join(ans))