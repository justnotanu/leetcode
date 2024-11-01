class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty list to store the result
        result = []
        
        # Initialize a counter for consecutive characters
        count = 0
        
        for i in range(len(s)):
            # If it's the first character or different from the last added character
            if i == 0 or s[i] != s[i - 1]:
                count = 1  # Reset count for new character
            else:
                count += 1  # Increment count for same character
            
            # Append to result only if less than 3 consecutive characters
            if count < 3:
                result.append(s[i])
        
        return ''.join(result)
