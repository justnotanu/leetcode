class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []  # Initialize an empty list to store valid combinations
        
        def backtrack(start: int, path: List[int], remaining: int):
            if len(path) == k:  # Base case: if the current combination has k numbers
                if remaining == 0:  # Check if the sum equals n
                    results.append(path[:])  # Add a copy of the current path to results
                return
            
            for i in range(start, 10):  # Iterate through numbers 1 to 9
                if i > remaining:  # If the current number exceeds the remaining sum, stop
                    break
                
                path.append(i)  # Include the current number in the combination
                backtrack(i + 1, path, remaining - i)  # Recur with updated parameters
                path.pop()  # Backtrack: remove the last added number
        
        backtrack(1, [], n)  # Start backtracking from number 1
        return results  # Return the list of valid combinations
