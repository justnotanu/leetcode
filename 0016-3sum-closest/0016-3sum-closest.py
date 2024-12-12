class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        
        # Initialize the closest sum with a large value
        closest_sum = float('inf')
        
        # Step 2: Iterate through each number as a fixed element
        for i in range(n):
            # Avoid duplicate elements for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # Step 3: Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If we hit exactly the target, return immediately
                    return current_sum
        
        return closest_sum
        