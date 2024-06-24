# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
 

# Constraints:

# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
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
        This method calculates the number of unique paths in a binary tree that sum up to a given targetSum.  
  
        :param root: The root node of the binary tree. Type: TreeNode  
        :param targetSum: The target sum for the unique paths. Type: int  
        :return: The number of unique paths that sum up to the targetSum. Type: int  
        """  
        def dfs(root, val, cur, dic):  
            """  
            A depth-first search function to traverse the binary tree.  
  
            :param root: The current node being visited. Type: TreeNode  
            :param val: The target sum for the unique paths. Type: int  
            :param cur: The current sum of the path from the root to the current node. Type: int  
            :param dic: A dictionary to keep track of the frequency of each cumulative sum. Type: {int: int}  
            """  
            if not root:  
                # If the current node is None (reached a leaf or went out of bounds), return.  
                return  
  
            # Update the current sum by adding the value of the current node.  
            cur += root.val  
  
            # Calculate the previous sum (before adding the current node's value)  
            pre = cur - val  
  
            # Check if there was a path that summed up to 'pre' before adding the current node's value.  
            # If so, add that count to the result.  
            self.res += dic.get(pre, 0)  
  
            # Update the dictionary to reflect the new cumulative sum.  
            dic[cur] = dic.get(cur, 0) + 1  
  
            # Recursively visit the left and right subtrees.  
            dfs(root.left, val, cur, dic)  
            dfs(root.right, val, cur, dic)  
  
            # After visiting the left and right subtrees, decrement the count of the current cumulative sum.  
            dic[cur] -= 1  
  
        # Initialize the result variable to 0.  
        self.res = 0  
  
        # Initialize a dictionary with 0 as the key and 1 as the value. This represents the path starting from the root with sum 0.  
        dic = {0: 1}  
  
        # Start the depth-first search from the root node.  
        dfs(root, targetSum, 0, dic)  
  
        # Return the final result.  
        return self.res