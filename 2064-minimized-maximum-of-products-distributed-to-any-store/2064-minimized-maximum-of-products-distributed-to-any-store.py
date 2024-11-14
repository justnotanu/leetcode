class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Binary search boundaries
        left, right = 1, max(quantities)
        
        while left < right:
            mid = (left + right) // 2
            
            # Calculate total stores needed for current mid
            total_stores_needed = 0
            for quantity in quantities:
                total_stores_needed += (quantity + mid - 1) // mid  # Equivalent to ceil(quantity / mid)
            
            # If we need more stores than available, increase mid
            if total_stores_needed > n:
                left = mid + 1
            else:
                right = mid
        
        return left
