# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

from collections import List 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # ans = [0] * n

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if temperatures[j] > temperatures[i]:
        #             ans[i] = j - i  # Record the number of days it took to reach a warmer day
        #             break  # Stop the loop once a warmer day is found
        
        # return ans

        n = len(temperatures)
        ans = [0] * n
        stack = []  # Stack to store indices of the temperatures list

        for curr_day,curr_temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return ans