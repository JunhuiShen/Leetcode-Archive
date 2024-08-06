# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 

# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # there are 3 actions to do: insert, delete, or replace
        m,n = len(word1), len(word2)

        if m == 0:
            return n
        
        if n == 0:
            return m
        
        distance_matrix = []
        for i in range(m + 1):
            row = [0] * (n + 1)
            distance_matrix.append(row)  
        
        for i in range(m+1):
            distance_matrix[i][0] = i
        
        for j in range(n+1):
            distance_matrix[0][j] = j
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    distance_matrix[i][j] = distance_matrix[i-1][j-1]
                else:
                    add = distance_matrix[i][j-1] + 1
                    delete =  distance_matrix[i-1][j] + 1
                    replace = distance_matrix[i-1][j-1] + 1
                    distance_matrix[i][j] = min(add,delete,replace)
        
        return distance_matrix[m][n]