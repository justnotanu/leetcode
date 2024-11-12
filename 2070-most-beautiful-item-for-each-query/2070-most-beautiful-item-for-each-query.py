class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items based on price and then by beauty
        items.sort()
        
        # Create a list to store prices and corresponding max beauties
        prices = []
        max_beauties = []
        
        current_max_beauty = 0
        
        # Build the prices and max_beauties lists
        for price, beauty in items:
            current_max_beauty = max(current_max_beauty, beauty)
            prices.append(price)
            max_beauties.append(current_max_beauty)
        
        # Prepare an answer list for queries
        answer = []
        
        # Process each query
        for query in queries:
            # Use binary search to find the right position
            idx = bisect.bisect_right(prices, query) - 1
            
            if idx >= 0:
                answer.append(max_beauties[idx])  # Get the max beauty for this price range
            else:
                answer.append(0)  # No item available for this query
        
        return answer
        