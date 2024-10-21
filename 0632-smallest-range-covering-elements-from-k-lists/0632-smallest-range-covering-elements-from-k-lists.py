class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list index, index in list)
            current_max = max(current_max, nums[i][0])
        
        best_range = [float('-inf'), float('inf')]
        
        while True:
            current_min, list_index, element_index = heapq.heappop(min_heap)
            
            # Update the best range if a smaller range is found
            if current_max - current_min < best_range[1] - best_range[0]:
                best_range = [current_min, current_max]
            
            # If we have exhausted one list, break
            if element_index + 1 == len(nums[list_index]):
                break
            
            # Push the next element from the same list into the heap
            next_value = nums[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
            current_max = max(current_max, next_value)

        return best_range
