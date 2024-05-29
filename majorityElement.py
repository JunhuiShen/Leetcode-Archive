# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

# My first attemp: it is correct but will exceed the time limit
# Brute Force with time complexity O(n^2)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcount = 0
        index = 0
        for i in range(len(nums)):
            count = 1
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > maxcount:
                maxcount = count
                index = i
        
        if maxcount > len(nums)//2:
            return nums[index]
        else:
            return 0
            
# Use sorting with time complexity O(n log(n))
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        return nums[len(nums)//2]        