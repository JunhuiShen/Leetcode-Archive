# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

 

# Example 1:



# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
# Example 2:



# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
# Example 3:

# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
 

# Constraints:

# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Define a helper function to perform depth-first search and count good nodes  
        def dfs(node, max_so_far):    
            # If the current node is None (end of a branch), return 0 good nodes  
            if node is None:   
                return 0  
            # If the value of the current node is greater than or equal to the max_so_far, it's a good node  
            count = 0  
            if node.val >= max_so_far:    
                count += 1  
            # Update the max_so_far value for the current subtree  
            max_so_far = max(node.val, max_so_far)  
            # Recursively count good nodes in the right and left subtrees, and add them to the count  
            count += dfs(node.right, max_so_far)  
            count += dfs(node.left, max_so_far)  
            # Return the total count of good nodes in the current subtree
            return count  

        # Start the depth-first search from the root node with an initial max_so_far value of negative infinity  
        # This ensures that all nodes will be considered as good nodes when compared against the initial value  
        return dfs(root, float("-inf"))  
