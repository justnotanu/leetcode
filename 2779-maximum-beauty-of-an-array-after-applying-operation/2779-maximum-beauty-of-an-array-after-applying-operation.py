class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        
        max_beauty = 0
        left = 0
        
        # Step 2: Use a sliding window approach
        for right in range(n):
            # Expand the right pointer until the condition is violated
            while nums[right] - nums[left] > 2 * k:
                left += 1
            
            # Calculate the size of the current valid window
            current_beauty = right - left + 1
            max_beauty = max(max_beauty, current_beauty)
        
        return max_beauty

        