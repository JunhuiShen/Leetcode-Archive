# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        # Initialize an empty list to store the nodes
        newlist = []

        current = head
        # Traverse the linked list and append each node to newlist
        while current:
            newlist.append(current)
            current = current.next
        
        newlist.reverse()

        for i in range(len(newlist) - 1):
            newlist[i].next = newlist[i + 1]
        newlist[-1].next = None

        return newlist[0]