class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1  # Move left pointer to increase sum
                elif current_sum > 0:
                    right -= 1  # Move right pointer to decrease sum
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        
        return result
