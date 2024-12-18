from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy() # Initialize result with original prices
        stack = [] # Stack to keep track of indices
        
        for i in range(len(prices)):
            # While stack is not empty and current price is less than or equal to price at index of stack's top
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop() # Get the index for which we found a discount
                result[index] -= prices[i] # Apply the discount
            stack.append(i) # Add current index to stack
            
        return result
