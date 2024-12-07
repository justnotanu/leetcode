class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def canSplit(maxSize):
            operations = 0
            for num in nums:
                if num > maxSize:
                    # Calculate how many operations are needed to split this bag
                    # We need (num - 1) // maxSize splits
                    operations += (num - 1) // maxSize
                if operations > maxOperations:
                    return False
            return True
        
        left, right = 1, max(nums)
        answer = right
        
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                answer = mid  # mid is a valid answer, try for smaller
                right = mid - 1
            else:
                left = mid + 1  # mid is too small, increase it
        
        return answer
