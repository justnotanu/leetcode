class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Step 1: Create a max-heap (invert values for Python's min-heap)
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        # Step 2: Perform operations for k seconds
        for _ in range(k):
            # Get the largest pile (invert back to positive)
            max_gifts = -heapq.heappop(max_heap)
            # Calculate remaining gifts after taking some
            remaining_gifts = math.floor(math.sqrt(max_gifts))
            # Push back the updated pile into the heap
            heapq.heappush(max_heap, -remaining_gifts)
        
        # Step 3: Calculate total remaining gifts
        total_remaining = -sum(max_heap)  # Invert back to positive
        
        return total_remaining
        