class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        # Loop through the array, stopping at n-2 to avoid index out of range
        for i in range(n - 2):
            first = nums[i]
            second = nums[i + 1]
            third = nums[i + 2]
            
            # Check if first + third equals half of second
            if first + third == second / 2:
                count += 1
                
        return count
