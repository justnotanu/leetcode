class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        n = len(word)
        i = 0
        
        while i < n:
            char = word[i]
            count = 0
            
            # Count occurrences of the current character (up to 9)
            while i < n and word[i] == char:
                count += 1
                i += 1
            
            # Append full groups of 9
            while count > 9:
                comp += "9" + char
                count -= 9
            
            # Append the remaining count (which will be <= 9)
            if count > 0:
                comp += str(count) + char
        
        return comp
