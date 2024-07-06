# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        queue = collections.deque([root])

        max_sum = float("-inf")
        max_level = 0
        current_level = 1

        while queue:
            queue_length = len(queue)
            level_sum = 0

            for i in range(queue_length):
                res_node = queue.popleft()
                level_sum += res_node.val

                if res_node.left:  
                    queue.append(res_node.left)
                if res_node.right:
                    queue.append(res_node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            current_level += 1
        
        return max_level