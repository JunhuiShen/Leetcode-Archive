# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        def isnegative(x):
            return x < 0

        sign = 1
        if isnegative(x) == True:
            sign = -1
            x = -x

        rev_x = 0
        while x > 0:
            remainder = x % 10
            rev_x = 10 * rev_x + remainder
            x = x // 10
        
        rev_x = sign * rev_x
        
        if rev_x < -2 ** (31) or rev_x > 2 ** (31):
            return 0
        
        return rev_x

        