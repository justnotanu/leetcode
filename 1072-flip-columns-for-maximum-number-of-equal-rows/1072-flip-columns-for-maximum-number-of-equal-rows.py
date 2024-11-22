class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = Counter()
        
        for row in matrix:
            # Create a normalized version of the row
            if row[0] == 1:
                # Flip the row if the first element is 1
                normalized_row = tuple(1 - x for x in row)
            else:
                normalized_row = tuple(row)
            
            # Count this normalized row pattern
            count[normalized_row] += 1
        
        # Return the maximum count of any normalized pattern
        return max(count.values())

