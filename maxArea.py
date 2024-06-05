# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # # Brute force solution
        # if height is None:
        #     return 0
        
        # max_area = 0 
        # len_height = len(height)

        # for entry_height in range(len_height):
        #     current_height = height[entry_height]
        #     for nextentry_height in range(entry_height+1, len_height):
        #         next_height = height[nextentry_height]
        #         current_area = (nextentry_height - entry_height) * min(next_height,current_height)
        #         if current_area >= max_area:
        #             max_area = current_area
        
        # return max_area


        ## Two-pointer solution
        # Edge case: if the height list is None, return 0
        if height is None:
            return 0
        
        # Initialize the maximum area to 0
        max_area = 0 
        # Get the length of the height list
        len_height = len(height)

        # Initialize two pointers, left_entry starting from the beginning and right_entry from the end of the list
        left_entry = 0
        right_entry = len_height - 1

        # Use the two-pointer approach to find the maximum area
        while left_entry < right_entry:
            # Get the heights at the current pointers
            left_height = height[left_entry]
            right_height = height[right_entry]
            # Calculate the current area based on the shorter height and the distance between the pointers
            current_area = (right_entry - left_entry) * min(left_height, right_height)
            
            # Update max_area if the current area is greater than the previously recorded max_area
            if current_area > max_area:
                max_area = current_area
            
            # Move the pointer pointing to the shorter line inward
            # This is because the area is limited by the shorter height, and moving the shorter pointer inward might help find a taller height, potentially increasing the area
            if left_height <= right_height:
                left_entry += 1
            else:
                right_entry -= 1
        
        # Return the maximum area found
        return max_area
    
# # Example usage
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# solution = Solution()
# print(f"Max area: {solution.maxArea(height)}")  # Output should be 49