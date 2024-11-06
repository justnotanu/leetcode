class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count the number of set bits
        def count_set_bits(num):
            return bin(num).count('1')
        
        n = len(nums)
        previous_max = -inf  # Initialize previous maximum to negative infinity
        i = 0
        
        while i < n:
            # Count set bits for the current number
            current_bit_count = count_set_bits(nums[i])
            current_min = nums[i]
            current_max = nums[i]
            
            # Move through the array to find all consecutive numbers with the same bit count
            while i < n and count_set_bits(nums[i]) == current_bit_count:
                current_min = min(current_min, nums[i])
                current_max = max(current_max, nums[i])
                i += 1
            
            # Check if previous max is less than current min
            if previous_max > current_min:
                return False
            
            # Update previous_max to current_max for next iteration
            previous_max = current_max
        
        return True
