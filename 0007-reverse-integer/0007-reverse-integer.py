class Solution:
    def reverse(self, x: int) -> int:
        # Define the bounds for signed 32-bit integers
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        # Determine if x is negative
        negative = x < 0
        x_abs = abs(x)
        
        # Reverse the digits
        reversed_x = int(str(x_abs)[::-1])
        
        # Restore sign
        if negative:
            reversed_x = -reversed_x
        
        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
        