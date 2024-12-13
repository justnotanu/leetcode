class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n  # Step 1: Create a marking array
        indexed_nums = [(num, i) for i, num in enumerate(nums)]  # Pair each number with its index
        
        # Step 2: Sort by value (and index implicitly)
        indexed_nums.sort()
        
        score = 0
        
        # Step 3: Iterate through sorted numbers
        for value, index in indexed_nums:
            if not marked[index]:  # If this number is not marked
                score += value  # Add its value to the score
                marked[index] = True  # Mark this number
                
                # Mark adjacent elements if they exist
                if index > 0:
                    marked[index - 1] = True  # Mark left neighbor
                if index < n - 1:
                    marked[index + 1] = True  # Mark right neighbor
        
        return score
        