class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n  # Not enough elements to form a mountain
        
        # Calculate LIS for each index
        lis = [0] * n
        dp = []
        for i in range(n):
            pos = bisect.bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            lis[i] = pos + 1  # Length of LIS ending at i

        # Calculate LDS for each index
        lds = [0] * n
        dp.clear()  # Reuse dp array for LDS
        for i in range(n - 1, -1, -1):
            pos = bisect.bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            lds[i] = pos + 1  # Length of LDS starting at i

        max_mountain_length = 0
        
        # Calculate maximum mountain length
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # Valid peak must have at least one element on each side
                max_mountain_length = max(max_mountain_length, lis[i] + lds[i] - 1)
        
        # Minimum removals to form a mountain array
        return n - max_mountain_length if max_mountain_length >= 3 else n
