# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isunique(str,i,j):
            chars = set() # keep track of characters encountered in the substring
            for k in range(i,j+1):
                char = str[k]
                if char in chars:
                    return False
                chars.add(char)
            return True

        n = len(s)
        length = 0
        for i in range(n):
            for j in range(i,n):
                if isunique(s,i,j):
                    length = max(length,j - i + 1)
        return length


solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)  # Output: -321
