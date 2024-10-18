class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Initialize a stack to keep track of indices of potential ramp starts
        stack = []
        
        # Iterate through the array to fill the stack with indices
        for index, value in enumerate(nums):
            # Only push indices where the current value is less than the last value in the stack
            if not stack or nums[stack[-1]] > value:
                stack.append(index)
        
        max_width = 0
        
        # Iterate from the end of the array to find the maximum ramp width
        for i in range(len(nums) - 1, -1, -1):
            # While there are indices in the stack and the current number is greater than or equal to the number at those indices
            while stack and nums[stack[-1]] <= nums[i]:
                # Calculate width and update max_width if necessary
                max_width = max(max_width, i - stack.pop())
            # If the stack is empty, break early as no more ramps can be found
            if not stack:
                break
        
        return max_width               