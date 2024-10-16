class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max-heap based on character counts
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        
        result = []
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count  # Convert back to positive
            
            # Check if we can add this character
            if len(result) >= 2 and result[-1] == result[-2] == char:
                # If adding this would create three in a row, check for next character
                if not max_heap:
                    break  # No alternative character available
                
                next_count, next_char = heapq.heappop(max_heap)
                next_count = -next_count
                
                # Add the next character instead
                result.append(next_char)
                next_count -= 1
                
                # Push back if there's still remaining count
                if next_count > 0:
                    heapq.heappush(max_heap, (-next_count, next_char))
                
                # Push back the original character since we didn't use it
                heapq.heappush(max_heap, (-count, char))
            else:
                # Add this character
                result.append(char)
                count -= 1
                
                # Push back if there's still remaining count
                if count > 0:
                    heapq.heappush(max_heap, (-count, char))
        
        return ''.join(result)
