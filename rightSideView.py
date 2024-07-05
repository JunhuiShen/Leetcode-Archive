# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        
        # # Initialize the result list which will store the rightmost nodes' values at each level
        array = []

        # # Initialize the queue with the root node for level-order traversal (BFS)
        queue = collections.deque([root])
        
        while queue:
            rightside = None
            queue_length = len(queue) # number of nodes in the currrent layer

            for i in range(queue_length):
                # pop the node from the left
                res_node = queue.popleft()
                if res_node:
                    # record the rightmost node in the current layer
                    rightside = res_node
                    # enqueue left child first so right child will be processed last at the current level
                    if res_node.left:  
                        queue.append(res_node.left)
                    if res_node.right:
                        queue.append(res_node.right)

            if res_node:
                # after processing all nodes at the current level, append the value of the rightmost node to the result list
                array.append(res_node.val)
        
        return array