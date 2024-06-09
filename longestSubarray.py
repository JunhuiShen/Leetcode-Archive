# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# Sliding window
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check for an edge case where the input list is None
        if nums is None:
            return 0  # If the input is None, return 0 as there are no elements to process

        # Initialize variables
        max_count = 0  # This will store the maximum length of the subarray of 1s found
        left_entry = 0  # This is the left pointer for the sliding window
        element_take = False  # This flag indicates whether we have taken a zero in the current window

        # Use a for loop to iterate over the list with the right pointer
        for right_entry in range(len(nums)):  # Right pointer for the sliding window, iterates through the list
            if nums[right_entry] == 0:  # If the current element is zero
                if element_take:  # Check if we have already taken a zero
                    # If we have taken a zero before, move the left pointer to the right until we find a zero
                    while nums[left_entry] != 0:
                        left_entry += 1
                    left_entry += 1  # Move the left pointer past the zero to remove it from the window
                else:
                    element_take = True  # Mark that we have taken a zero

            # Calculate the current length of the window
            current_count = right_entry - left_entry

            # Update max_count if the current window length is larger
            max_count = max(max_count, current_count)

        # Return the maximum length of the subarray found
        return max_count

# Example usage:
solution = Solution()
print(solution.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # Expected output: 5
            

