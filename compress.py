# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
 

# Constraints:

# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars) # Get the lengths of chas

        compress_entry = 0 # Pointer to write the compressed character
        chars_entry = 0 # # Pointer to read the characters
        
        if n == 0:
            return 0 # Handle the edge case of an empty list

        while chars_entry < n:
            current_char = chars[chars_entry] # Current character to process
            group_length = 0 # Counter for occurrences of the current character

            # Count the occurrences of the current character
            while chars_entry < n and chars[chars_entry] == current_char:
                chars_entry += 1
                group_length += 1

             # Write the character to the compressed list
            chars[compress_entry] = current_char
            compress_entry += 1

            # If the character appears more than once, write the count as well
            if group_length > 1:
                chars[compress_entry] = str(group_length)

                # This is in case we need to print numbers 12 using "1","2"
                for length in str(group_length):
                    chars[compress_entry] = length
                    compress_entry += 1
            
        return compress_entry  # Return the length of the compressed list

# # Example usage:
# solution = Solution()
# chars = ["a", "a", "b", "b", "c", "c", "c"]
# length = solution.compress(chars)
# print(chars[:length])  # Output should be ['a', '2', 'b', '2', 'c', '3']