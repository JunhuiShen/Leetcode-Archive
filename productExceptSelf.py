# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        length = len(nums)
        left_products = [0] * length
        right_products = [0] * length
        result = [0] * length

        # Initialize the first element of left_products
        left_products[0] = 1
        # Fill left_products such that left_products[i] contains the product of all elements to the left of nums[i]
        for i in range(1, length):
            left_products[i] = nums[i - 1] * left_products[i - 1]

        # Initialize the last element of right_products
        right_products[length - 1] = 1
        # Fill right_products such that right_products[i] contains the product of all elements to the right of nums[i]
        for i in range(length - 2, -1, -1):
            right_products[i] = nums[i + 1] * right_products[i + 1]

        # Construct the result array where result[i] is the product of all elements except nums[i]
        for i in range(length):
            result[i] = left_products[i] * right_products[i]

        return result