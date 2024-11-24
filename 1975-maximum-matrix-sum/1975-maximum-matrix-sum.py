class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_value = float('inf')  # Initialize to infinity
        
        # Iterate through each element in the matrix
        for row in matrix:
            for value in row:
                total_sum += abs(value)  # Add absolute value to total sum
                min_abs_value = min(min_abs_value, abs(value))  # Update minimum absolute value
                
                if value < 0:  # Count negative numbers
                    negative_count += 1
        
        # If there is an even number of negatives, return total_sum
        if negative_count % 2 == 0:
            return total_sum
        else:
            # If odd, subtract twice the minimum absolute value
            return total_sum - 2 * min_abs_value
