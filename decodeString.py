class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Initialize a stack to keep track of characters and partial results
        stack = []
        
        # Iterate through each character in the input string
        for i in range(len(s)):
            if s[i] != "]":
                # If the current character is not a closing bracket, push it onto the stack
                stack.append(s[i])
            else:
                # When a closing bracket is encountered, start forming the substring
                substring = ""
                # Pop characters from the stack until an opening bracket is found, building the substring
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                # Remove the opening bracket from the stack
                stack.pop()

                # Now, we need to find the number associated with the substring
                int_string = ""
                # Pop characters from the stack as long as they are digits, forming the complete number
                while stack and stack[-1].isdigit():
                    int_string = stack.pop() + int_string
                
                # Repeat the substring int(int_string) times and push the result back onto the stack
                stack.append(int(int_string) * substring)
            
        # Join all elements in the stack to form the final decoded string
        return "".join(stack)

# This implementation is based on the explanation provided in the following video:
# https://www.youtube.com/watch?v=qB0zZpBJlh8