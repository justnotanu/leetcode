class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find sorted prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        # If already fully sorted
        if left == n - 1:
            return 0
        
        # Step 2: Find sorted suffix
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        
        # Step 3: Calculate minimum length to remove
        min_length = min(n - left - 1, right)  # Remove either from start or end
        
        # Step 4: Check for overlaps between prefix and suffix
        j = right
        for i in range(left + 1):
            while j < n and arr[j] < arr[i]:
                j += 1
            if j < n:
                min_length = min(min_length, j - i - 1)
        
        return min_length
        