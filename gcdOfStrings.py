# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Get the lengths of the input strings str1 and str2
        len1 = len(str1)
        len2 = len(str2)
        
        # Define a helper function to check 
        # if a given length k is a valid divisor for both strings
        def valid(k):
            # If k does not evenly divide either of the string lengths, 
            # it's not a valid length
            if len1 % k != 0 or len2 % k != 0:
                return False
            # Determine how many times the base substring of length k would need to repeat
            # to match the lengths of str1 and str2
            n1 = len1 // k
            n2 = len2 // k
            # Extract the base substring from str1
            base = str1[:k]
            # Check if repeating the base substring n1 times forms str1
            # and repeating it n2 times forms str2
            return str1 == n1 * base and str2 == n2 * base
        
        # Determine the minimum length between the two strings
        min_length = min(len1, len2)
        
        # Iterate from the minimum length down to 1
        # This ensures we find the longest possible valid substring
        for i in range(min_length, 0, -1):
            # If the current length i is a valid divisor length for both strings,
            # return the corresponding substring of length i from str1
            if valid(i):
                return str1[:i]
        
        # If no valid substring is found, return an empty string
        return ""