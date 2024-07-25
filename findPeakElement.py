# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # brute force search
        # for i in range(len(nums)-1):
        #     if i == 0 and len(nums) > 1 and nums[i] > nums[i + 1]:
        #         return i
        #     elif i == len(nums) - 1 and nums[i] > nums[i - 1]:
        #         return i
        #     elif 0 < i < len(nums) - 1 and nums[i] > nums[i + 1] and nums[i] > nums[i - 1]:
        #         return i
        # return 0

        def search(nums, left, right):
            # Base case: one element left
            if left == right:
                return left
            
            # Calculate midpoint
            middle = (left + right) // 2

            # Compare middle element with its next neighbor
            if nums[middle] > nums[middle + 1]:
                # If middle element is greater, search left half (including middle)
                return search(nums, left, middle)
            else:
                # If middle element is smaller, search right half (excluding middle)
                return search(nums, middle + 1, right)
        
        # Start the search with the full range of the array
        return search(nums, 0, len(nums) - 1)