class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are equal; if not, return False
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself
        doubled_s = s + s
        
        # Check if goal is a substring of the concatenated string
        return goal in doubled_s
        