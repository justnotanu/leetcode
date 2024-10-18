class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Create a max-heap (invert values for Python's min-heap)
        max_heap = [-num for num in nums]  # Store negative values to simulate max-heap
        heapq.heapify(max_heap)
        
        total_score = 0
        
        for _ in range(k):
            # Get the maximum element
            max_value = -heapq.heappop(max_heap)  # Pop and negate back to positive
            total_score += max_value  # Add to total score
            
            # Calculate new value and push back into heap
            new_value = math.ceil(max_value / 3)
            heapq.heappush(max_heap, -new_value)  # Push back as negative
            
        return total_score