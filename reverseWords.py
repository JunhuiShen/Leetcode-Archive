# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. 
# The returned string should only have a single space separating the words. Do not include any extra spaces.

 

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split the string into a list of words
        # "the sky is blue" -> ["the", "sky", "is", "blue"]
        words = s.split()

        # Reverse the order of words in the list
        # ["the", "sky", "is", "blue"] -> ["blue","is","sky","the"]
        reversed_words = words[::-1]

        # Join the reversed list of words into a new string
        reversed_string = " ".join(reversed_words)
        return reversed_string

# # Example usage
# solution = Solution()
# result = solution.reverseWords("the sky is blue")
# print(result)  # Output: "blue is sky the"