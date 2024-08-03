# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. 
# Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. 
# Two tilings are different if and only if there are two 4-directionally 
# adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

# Example 1:


# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
# Example 2:

# Input: n = 1
# Output: 1
 

# Constraints:

# 1 <= n <= 1000

class Solution:
    def numTilings(self, n: int) -> int:
        # Define the modulo constant to avoid large numbers
        mod = 10 ** 9 + 7

        # Base cases for n < 2
        if n < 2:
            return n
        
        # Initialize arrays to store solutions for subproblems
        f = [0] * (n + 1)  # f[k] represents the number of ways to tile a 2xk board
        p = [0] * (n + 1)  # p[k] represents a helper state for partial tilings
        
        # Base cases: precompute for small values of k
        f[1] = 1  # One way to tile a 2x1 board (a single vertical domino)
        f[2] = 2  # Two ways to tile a 2x2 board (two vertical dominoes or two horizontal dominoes)
        p[2] = 1  # One valid partial tiling that can contribute to larger tilings
        
        # Fill the arrays for larger values of k using the recurrence relations
        for k in range(3, n + 1):
            # f[k] = (ways to tile 2x(k-1)) + (ways to tile 2x(k-2)) + (ways involving trominoes)
            f[k] = (f[k-1] + f[k-2] + 2 * p[k-1]) % mod
            
            # Update the helper state p[k], which helps in calculating future f[k] values
            p[k] = (p[k-1] + f[k-2]) % mod
        
        # Return the final result, which is the number of ways to tile a 2xn board
        return f[n]