class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Count occurrences of each bit position being set
        count = [0] * 32  # Since candidates[i] <= 10^7, we need up to 27 bits
        
        for num in candidates:
            for j in range(32):
                if num & (1 << j):  # Check if j-th bit is set
                    count[j] += 1
        
        # The largest combination size will be the maximum count found
        return max(count)
        