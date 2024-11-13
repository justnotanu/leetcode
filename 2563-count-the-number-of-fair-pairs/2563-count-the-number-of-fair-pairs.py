class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the input array
        nums.sort()
        count = 0
        n = len(nums)
        
        # Iterate through each element in the sorted array
        for i in range(n):
            # Calculate the bounds for binary search
            min_value = lower - nums[i]
            max_value = upper - nums[i]
            
            # Find the left index (first position where nums[j] >= min_value)
            left_index = bisect.bisect_left(nums, min_value, i + 1)
            # Find the right index (first position where nums[j] > max_value)
            right_index = bisect.bisect_right(nums, max_value, i + 1)
            
            # The number of valid pairs with this i is (right_index - left_index)
            count += right_index - left_index
        
        return count
        