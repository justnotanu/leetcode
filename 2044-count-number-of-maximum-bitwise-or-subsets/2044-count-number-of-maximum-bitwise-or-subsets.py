class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        
        # Step 1: Calculate the maximum bitwise OR
        for num in nums:
            max_or |= num
        
        # Step 2: Count subsets that yield max_or
        count = 0
        n = len(nums)
        
        # There are 2^n - 1 non-empty subsets
        for i in range(1, 1 << n):  # Loop from 1 to 2^n - 1
            subset_or = 0
            
            for j in range(n):
                if i & (1 << j):  # Check if jth element is included in the subset
                    subset_or |= nums[j]  # Update the OR for this subset
            
            if subset_or == max_or:
                count += 1
        
        return count
