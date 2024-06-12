# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
# If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        newlist = []  # This stack will store the surviving asteroids

        for asteroid in asteroids:
            while newlist and asteroid < 0 < newlist[-1]:
                if newlist[-1] < -asteroid:
                    newlist.pop()  # The top of the stack is smaller, so it gets destroyed
                    continue  # Continue to compare the current asteroid with the new top
                elif newlist[-1] == -asteroid:
                    newlist.pop()  # Both asteroids destroy each other
                break  # The current asteroid gets destroyed; no need to push it to the stack
            else:
                newlist.append(asteroid)  # No collision, so push the current asteroid to the stack
        
        return newlist  # The stack now contains all the surviving asteroids