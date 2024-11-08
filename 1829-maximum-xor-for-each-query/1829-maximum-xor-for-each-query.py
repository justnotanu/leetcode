class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate total XOR of all elements
        total_xor = 0
        for num in nums:
            total_xor ^= num
        
        # Maximum value for k based on maximumBit
        max_k = (1 << maximumBit) - 1
        
        # Prepare answer list
        answer = []
        
        # Process queries from last element to first
        for num in reversed(nums):
            # Calculate k for current state
            k = total_xor ^ max_k
            answer.append(k)
            # Remove current number from total_xor
            total_xor ^= num
        
        return answer
        