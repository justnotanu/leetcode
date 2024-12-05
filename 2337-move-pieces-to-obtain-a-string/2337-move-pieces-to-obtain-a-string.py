class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Check if the counts of 'L' and 'R' match
        if start.replace('_', '').count('L') != target.replace('_', '').count('L'):
            return False
        if start.replace('_', '').count('R') != target.replace('_', '').count('R'):
            return False
        
        n = len(start)
        i, j = 0, 0
        
        while i < n and j < n:
            # Move i to the next non-blank character in start
            while i < n and start[i] == '_':
                i += 1
            # Move j to the next non-blank character in target
            while j < n and target[j] == '_':
                j += 1
            
            # If both pointers are at the end, we're done
            if i == n and j == n:
                return True
            
            # If one is at the end but not the other, return False
            if (i == n) != (j == n):
                return False
            
            # Check if characters match
            if start[i] != target[j]:
                return False
            
            # Check movement constraints
            if start[i] == 'L' and i < j:  # L cannot move right
                return False
            if start[i] == 'R' and i > j:  # R cannot move left
                return False
            
            # Move to the next characters
            i += 1
            j += 1
        
        return True
