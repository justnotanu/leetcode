class Solution:
    def countPairs(self, nums: List[int], mid: int) -> int:
        count = 0
        left = 0
        
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
            count += right - left  # Count pairs (left, right)
        
        return count

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array
        
        # Binary search for the smallest distance
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            if self.countPairs(nums, mid) < k:
                left = mid + 1  # We need a larger distance
            else:
                right = mid  # We can try a smaller distance
        
        return left  # The smallest distance with at least k pairs

        