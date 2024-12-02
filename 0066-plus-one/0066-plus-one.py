class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Start from the last digit
        for i in range(n - 1, -1, -1):
            digits[i] += 1  # Increment the current digit
            
            if digits[i] < 10:
                return digits  # No carry, return the result
            
            digits[i] = 0  # Set current digit to 0 if it becomes 10
        
        # If we are here, it means we have a carry that needs to be added
        return [1] + digits  # Prepend 1 to the list
