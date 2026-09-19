"""

------------------------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1293/B -------------------------------------------

Our dear Cafe's owner, JOE Miller, will soon take part in a new game TV-show "1 vs. n"!

The game goes in rounds, where in each round the host asks JOE and his opponents a common question. All participants failing to answer are eliminated. 
The show ends when only JOE remains (we assume that JOE never answers a question wrong!).

For each question JOE answers, if there are s (s > 0) opponents remaining and t (0 ≤ t ≤ s) of them make a mistake on it, 
JOE receives ts dollars, and consequently there will be s−t opponents left for the next question.

JOE wonders what is the maximum possible reward he can receive in the best possible scenario. Yet he has little time before show starts, so can you help him answering it instead?

Input
The first and single line contains a single integer n (1 ≤ n ≤ 10^5), denoting the number of JOE's opponents in the show.

Output
Print a number denoting the maximum prize (in dollars) JOE could have.

Your answer will be considered correct if it's absolute or relative error won't exceed 10−4. In other words, if your answer is a and the jury answer is b, then it must hold that |a−b|max(1,b)≤10^−4.

Input:
1

Output:
1.00000000000
"""
n = int(input())
gamma = 0.5772156649015329 
ans = sum(1 / i for i in range(1, n + 1))
print(ans)