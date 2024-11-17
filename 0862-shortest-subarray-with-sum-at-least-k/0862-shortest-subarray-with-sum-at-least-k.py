class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Step 1: Compute prefix sums
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        # Step 2: Initialize deque and minimum length
        min_length = float('inf')
        dq = deque()
        
        # Step 3: Iterate over prefix sums
        for i in range(n + 1):
            # Check if we can form a valid subarray
            while dq and prefix_sums[i] - prefix_sums[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())
            
            # Maintain increasing order in deque
            while dq and prefix_sums[i] <= prefix_sums[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        
        return min_length if min_length != float('inf') else -1

        