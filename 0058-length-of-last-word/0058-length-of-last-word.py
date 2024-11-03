class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip any trailing spaces from the string
        s = s.rstrip()
        
        # Split the string into words using spaces
        words = s.split(' ')
        
        # Return the length of the last word
        return len(words[-1])