# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Initialize the variables
        max_count = 0  # To store the maximum number of consecutive 1s
        count = 0      # To count the current number of 1s in the sequence
        zero_used = 0  # Counter to track the number of 0s included in the current sequence
        left = 0       # Pointer to manage the sliding window of elements

        # Iterate through the list with the right pointer
        for right in range(len(nums)):
            if nums[right] == 1:
                # If the current element is 1, increment the count
                count += 1
            elif zero_used < k:
                # If the current element is 0 and we can still flip a 0 to 1
                # Include this zero in the count and increment the zero_used counter
                count += 1
                zero_used += 1
            else:
                # If the current element is 0 and we've already used k flips,
                # move the left pointer to skip elements until we pass a zero
                while nums[left] == 1:
                    # Decrease the count for each 1 skipped
                    count -= 1
                    left += 1  # Move the left pointer to the right
                # Move past the zero at the left pointer
                left += 1

            # Update the max_count if the current count is greater
            max_count = max(max_count, count)

        return max_count
        