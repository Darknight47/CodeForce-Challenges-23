"""

------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/733/A --------------------------

One day, the Grasshopper was jumping on the lawn and found a piece of paper with a string. 
Grasshopper became interested what is the minimum jump ability he should have in order to be able to reach the far end of the string, jumping only on vowels of the English alphabet. 
Jump ability is the maximum possible length of his jump.

Formally, consider that at the begginning the Grasshopper is located directly in front of the leftmost character of the string. 
His goal is to reach the position right after the rightmost character of the string. In one jump the Grasshopper could jump to the right any distance from 1 to the value of his jump ability.

The following letters are vowels: 'A', 'E', 'I', 'O', 'U' and 'Y'.

Input
The first line contains non-empty string consisting of capital English letters. It is guaranteed that the length of the string does not exceed 100.

Output
Print single integer a — the minimum jump ability of the Grasshopper (in the number of symbols) that is needed to overcome the given string, jumping only on vowels.

Input:
ABABBBACFEYUKOTT

Output:
4
"""
vowels = 'AEIOUY'
s = input()
ans = 0
prev = 0
for i in range(len(s)):
    if(s[i] in vowels):
        temp = (i + 1) - prev
        prev = i + 1
        if(temp > ans):
            ans = temp
if((len(s) + 1) - prev > ans):
    ans = (len(s) + 1) - prev
print(ans)