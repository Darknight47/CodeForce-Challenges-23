"""

------------------------------- Link for the challenge: https://codeforces.com/gym/106711/problem/B --------------------------

(The only difference between the easy and hard versions is the constraint on n.)

It's game day, and students are in DKR, eagerly watching the scoreboard clock counting down to kickoff. 
The countdown is displayed as n mechanical flip-digit indicators, each showing a digit from 0−9.

The clock is weird; when the display ticks down from t to t−1, the digits do not flip all instantly. 
Instead, each digit that needs to change takes 1 second to flip. But digits can only be flipped once at a time.

So, for instance, if the clock ticks down from 67 to 66, it only takes 1 second, as only one digit changed. But if the clock ticks down from 900 to 899, it takes 3 seconds, as three digits changed.

Given how many seconds are currently displayed on the clock, the students are wondering how many actual seconds it will take until kickoff (when the clock has all digits showing 0).

Input
The first line will contain n (1≤n≤6), the number of digits of the number.

The second line will be a string of n digits, the current display on the clock. It is guaranteed that at least one digit is not zero.

Output
Print a single integer without leading zeros, the number of actual seconds left until kickoff.


"""
n = int(input())
num = int(input())

total_time = num
divisor = 10

while divisor <= num:
    total_time += num // divisor
    divisor *= 10

print(total_time)