class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1 or greater than or equal to length of s
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array of strings for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False  # Direction flag
        
        # Iterate over each character in the string
        for char in s:
            rows[current_row] += char
            
            # Change direction if we hit the top or bottom row
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False
            
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Join all rows to get the final result
        return ''.join(rows)
