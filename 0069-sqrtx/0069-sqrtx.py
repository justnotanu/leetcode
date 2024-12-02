class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # The square root of 0 is 0, and of 1 is 1
        
        left, right = 0, x
        
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # The largest integer whose square is less than or equal to x
        