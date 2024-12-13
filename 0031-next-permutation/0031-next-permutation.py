class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Step 1: Find the pivot
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  # If there is a pivot
            # Step 2: Find the successor
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap pivot and successor
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])

"""
        Do not return anything, modify nums in-place instead.
        """
        