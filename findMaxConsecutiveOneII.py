Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: 
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize the variables
        max_count = 0  # To store the maximum number of consecutive 1s
        count = 0      # To count the current number of 1s in the sequence
        zero_used = False  # Flag to indicate if a zero has been included in the current sequence
        left = 0      # Pointer to manage the sliding window of consecutive 1s plus at most one zero

        # Iterate through the list with the right pointer
        for right in range(len(nums)):
            if nums[right] == 1:
                # If the current element is 1, increment the count
                count += 1
            elif not zero_used:
                # If the current element is 0 and we haven't used a zero yet,
                # include this zero in the count and set the zero_used flag to True
                count += 1
                zero_used = True
            else:
                # If the current element is 0 and we've already used a zero,
                # move the left pointer to skip elements until the previous zero is passed
                while nums[left] == 1:
                    count -= 1  # Decrease the count for each 1 skipped
                    left += 1   # Move the left pointer to the right
                left += 1       # Move past the zero

            # Update the max_count if the current count is greater
            max_count = max(max_count, count)

        return max_count