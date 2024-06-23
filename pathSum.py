# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
# Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
# Example 2:


# Input: root = [1,2,3], targetSum = 5
# Output: []
# Example 3:

# Input: root = [1,2], targetSum = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):  
    def pathSum(self, root, targetSum):  
        """  
        Compute all unique paths which sum up to a given targetSum from a binary tree.  
          
        Each path should be represented as a list of the node's values, starting from the root and ending at some leaf node.  
  
        Args:  
            root (TreeNode): The root node of the binary tree.  
            targetSum (int): The target sum to find in the binary tree.  
  
        Returns:  
            List[List[int]]: A list of lists, where each inner list represents a unique path in the tree that sums up to the targetSum.  
  
        """  
        def dfs(node, current_sum, path, result):  
            # Base case: If the current node is None (we've reached a non-existent path), return immediately.  
            if not node:    
                return    
  
            # Add the current node's value to the path and update the current sum.  
            path.append(node.val)    
            current_sum -= node.val   
  
            # If we've reached a leaf node and the current sum is zero, it means we've found a valid path.  
            # Add this path to the result list.  
            if not node.left and not node.right and current_sum == 0:    
                result.append(list(path))  # Make a copy of the path to avoid modifying the original list.  
  
            # Recursively explore the left and right subtrees.  
            dfs(node.left, current_sum, path, result)    
            dfs(node.right, current_sum, path, result)    
  
            # After exploring both subtrees, remove the current node's value from the path to backtrack.  
            path.pop()    
  
        # Initialize the result list and call the recursive helper function.  
        result = []    
        dfs(root, targetSum, [], result)    
        return result  