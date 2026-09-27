"""

------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1133/A ------------------------------

Polycarp is going to participate in the contest. It starts at h1:m1 and ends at h2:m2. 
It is guaranteed that the contest lasts an even number of minutes (i.e. m1%2=m2%2, where x%y is x modulo y). 
It is also guaranteed that the entire contest is held during a single day. 
And finally it is guaranteed that the contest lasts at least two minutes.

Polycarp wants to know the time of the midpoint of the contest. 
For example, if the contest lasts from 10:00 to 11:00 then the answer is 10:30, if the contest lasts from 11:10 to 11:12 then the answer is 11:11.

Input
The first line of the input contains two integers h1 and m1 in the format hh:mm.

The second line of the input contains two integers h2 and m2 in the same format (hh:mm).

It is guaranteed that 0≤h1,h2≤23 and 0≤m1,m2≤59.

It is guaranteed that the contest lasts an even number of minutes (i.e. m1%2=m2%2, where x%y is x modulo y). 
It is also guaranteed that the entire contest is held during a single day. And finally it is guaranteed that the contest lasts at least two minutes.

Output
Print two integers h3 and m3 (0 ≤ h3 ≤ 23, 0 ≤ m3 ≤ 59) corresponding to the midpoint of the contest in the format hh:mm. 
Print each number as exactly two digits (prepend a number with leading zero if needed), separate them with ':'.

Input:
10:00
11:00

Output:
10:30
"""
firstHour, firstMin = input().split(":")
secondHour, secondMin = input().split(":")
firstHour = int(firstHour)
firstMin = int(firstMin)
secondHour = int(secondHour)
secondMin = int(secondMin)

total_first_min = (firstHour * 60) + firstMin
total_sec_min = (secondHour * 60) + secondMin
diff_min = total_sec_min - total_first_min
temp = total_first_min + (diff_min // 2)
ans_hour = temp // 60
ans_min = temp % 60
print(f"{ans_hour:02}:{ans_min:02}")