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

        # # Define a helper function to check if all characters in the substring s[i:j+1] are unique
        # def isunique(str, i, j):
        #     chars = set()  # Create a set to keep track of characters encountered in the substring
        #     for k in range(i, j + 1):  # Iterate through each character in the substring
        #         char = str[k]  # Get the character at index k
        #         if char in chars:  # If the character is already in the set, the substring is not unique
        #             return False
        #         chars.add(char)  # Add the character to the set
        #     return True  # If no duplicates are found, return True
        
        # n = len(s)  # Get the length of the input string s
        # length = 0  # Initialize the variable to store the length of the longest unique substring
        # for i in range(n):  # Iterate over each possible starting index of the substring
        #     for j in range(i, n):  # Iterate over each possible ending index of the substring
        #         if isunique(s, i, j):  # Check if the substring s[i:j+1] is unique
        #             length = max(length, j - i + 1)  # Update the maximum length if the current substring is longer
        # return length  # Return the length of the longest unique substring

        # Initialize the hash map to store the characters and their latest positions
        char_map = {}
        
        # Initialize the starting index of the sliding window and the maximum length
        left = 0
        max_length = 0

        # Iterate through the string with the right pointer of the sliding window
        for right in range(len(s)):
            # If the character is already in the hash map and its index is within the current window
            if s[right] in char_map and char_map[s[right]] >= left:
                # Move the left pointer to the right of the duplicate character's last known position
                left = char_map[s[right]] + 1

            # Update the hash map with the current character's position
            char_map[s[right]] = right
            
            # Calculate the current window length and update the maximum length if needed
            max_length = max(max_length, right - left + 1)

        # Return the length of the longest substring without repeating characters
        return max_length



