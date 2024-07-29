# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort candidates to facilitate the early stopping condition

        def backtrack(remain, comb, start):
            # Base case: if remain is 0, add the current combination to the result
            if remain == 0:
                result.append(list(comb))
                return
            
            # Iterate through the candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                current = candidates[i]
                # If the current candidate is greater than the remaining sum, stop further exploration
                if current > remain:
                    return
                
                # Include the current candidate in the combination
                comb.append(current)
                # Recurse with the updated remaining sum and the same start index (allowing reuse of the same element)
                backtrack(remain - current, comb, i)
                # Backtrack by removing the last added candidate
                comb.pop()
        
        # Start the backtracking with the target sum, empty combination, and starting index 0
        backtrack(target, [], 0)
        return result

