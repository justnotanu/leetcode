class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Initialize in-degrees array
        in_degree = [0] * n
        
        # Count in-degrees for each node
        for u, v in edges:
            in_degree[v] += 1
        
        # Find all teams with zero in-degree
        champions = [i for i in range(n) if in_degree[i] == 0]
        
        # Determine the result based on the number of potential champions
        if len(champions) == 1:
            return champions[0]
        else:
            return -1
        