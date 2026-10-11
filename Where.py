"""

--------------------------- Link for the challenge: https://codeforces.com/gym/106711/problem/A -------------------------------

The University of Texas Programming Club has lost track of where it is after staring at grid diagrams for too long. 
Fortunately, the club remembers one essential fact: Texas is shaped exactly like a size-1 plus sign. 
In this problem, a size-1 plus sign consists of five cells: a center cell and the four cells that share a side with it.

You are given an n×m map describing UTPC and its surroundings. Every cell is either open or blocked off. 
Count the number of ways to place a size-1 plus sign on the grid, lying on only open cells. 
Two placements are considered different if their center cells are different.

Input
The first line contains two integers n and m (1 ≤ n, m ≤ 100), the number of rows and columns of the map.

Each of the next n lines contains a string of m characters. A character "." represents an open cell, and a character "#" represents a blocked cell.

Output
Print one integer: the number of valid placements of Texas.

Input:
3 3
...
...
...

Output:
1
"""
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())
ans = 0

for r in range(1, n - 1):
    for c in range(1, m - 1):
        if(grid[r][c] == '.' and
           grid[r - 1][c] == '.' and
           grid[r + 1][c] == '.' and
           grid[r][c - 1] == '.' and
           grid[r][c + 1] == '.'):
            ans += 1

print(ans)