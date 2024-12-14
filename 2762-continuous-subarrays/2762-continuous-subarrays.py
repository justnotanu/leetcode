class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        total_count = 0
        
        # Deques to maintain minimum and maximum in the current window
        min_deque = deque()
        max_deque = deque()
        
        for right in range(n):
            # Maintain max deque
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min deque
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Ensure the current window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                # Remove indices that are out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Count valid subarrays ending at right
            total_count += (right - left + 1)
        
        return total_count
        