# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 
# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == "":
            return True

        position = 0
        len_s = len(s)
        len_t = len(t)
        count = 0
        for entry_s in range(len_s):
            for entry_t in range(position,len_t):
                if s[entry_s] == t[entry_t]:
                    position = entry_t + 1
                    count += 1
                    if count == len_s:
                        return True
                    break

        return False


# s = "abc"
# t = "ahbgdc"
# solution = Solution()
# Bool_value = solution.isSubsequence(s,t)
# print(Bool_value)