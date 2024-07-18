# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row, col = len(grid), len(grid[0])

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()

        fresh_count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        while queue:
            x, y, time = queue.popleft()

            for dx,dy in direction:
                nx,ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx,ny,time+1))
                    fresh_count -= 1
            
        if fresh_count == 0:
            return time
        else:
            return -1