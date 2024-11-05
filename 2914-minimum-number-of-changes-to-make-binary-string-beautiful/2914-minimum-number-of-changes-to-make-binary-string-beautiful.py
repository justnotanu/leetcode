class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        n = len(s)
        
        # Iterate through the string in steps of 2
        for i in range(0, n, 2):
            # Check if we are at the last character and handle it
            if i + 1 < n:
                if s[i] != s[i + 1]:
                    # If characters are different, we need to change one
                    changes += 1
        
        return changes
