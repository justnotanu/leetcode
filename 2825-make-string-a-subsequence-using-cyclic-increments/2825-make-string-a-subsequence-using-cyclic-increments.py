class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0  # Pointer for str2
        n = len(str2)
        
        for c in str1:
            # Calculate the next cyclic character
            next_char = 'a' if c == 'z' else chr(ord(c) + 1)
            
            # Check if we have matched all characters of str2
            if i < n and (str2[i] == c or str2[i] == next_char):
                i += 1  # Move to the next character in str2
            
            # If we have matched all characters of str2, return True
            if i == n:
                return True
        
        # If we finish iterating and haven't matched all characters, return False
        return i == n
