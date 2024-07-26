# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
 

# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum eating speed that allows eating all the bananas within h hours.
        
        Args:
        piles (List[int]): List of integers representing piles of bananas.
        h (int): The maximum number of hours allowed to eat all the bananas.

        Returns:
        int: The minimum integer eating speed.
        """
        
        # # Brute Force Approach
        # # Initialize the speed to 1.
        # speed = 1
        # while True:
        #     # Initialize the total hours spent with the current speed.
        #     hour_spent = 0
        #     # Calculate the total hours needed to eat all piles at the current speed.
        #     for pile in piles:
        #         hour_spent += math.ceil(pile / speed)
            
        #     # If the total hours spent is less than or equal to h, return the current speed.
        #     if hour_spent <= h:
        #         return speed
        #     else:
        #         # Increment the speed to try the next possible eating speed.
        #         speed += 1

        # Optimized Approach using Binary Search
        left = 1  # Minimum possible eating speed
        right = max(piles)  # Maximum possible eating speed

        # Perform binary search to find the minimum speed.
        while left < right:
            middle = (left + right) // 2  # Calculate the middle speed
            hour_spent = 0  # Initialize the total hours spent with this speed

            # Calculate the total hours needed to eat all piles at the current middle speed.
            for pile in piles:
                hour_spent += math.ceil(pile / middle)

            # If the total hours spent is less than or equal to h, search in the left half.
            if hour_spent <= h:
                right = middle
            # If the total hours spent is more than h, search in the right half.
            else:
                left = middle + 1

        # Return the minimum speed found.
        return right
