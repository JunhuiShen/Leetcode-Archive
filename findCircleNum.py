# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.

 

# Example 1:


# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:


# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
 

# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            # For each neighbor of the current node
            for neighbor, is_connected in enumerate(isConnected[node]):
                # Check if there is a connection and if the neighbor has not been visited
                if is_connected and neighbor not in visited:
                    # Mark the neighbor as visited
                    visited.add(neighbor)
                    # Perform DFS on the neighbor
                    dfs(neighbor)
        
        visited = set()  # To keep track of visited cities
        province_count = 0  # To count the number of provinces
        
        m = len(isConnected)  # Number of cities (rows in the matrix)
        
        # Iterate through each city
        for i in range(m):
            # If the city has not been visited, it means we found a new province
            if i not in visited:
                visited.add(i)  # Mark the city as visited
                dfs(i)  # Perform DFS to visit all connected cities
                province_count += 1  # Increment the province count
        
        return province_count