class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Initialize the graph with the initial roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)  # Add initial roads
        
        results = []
        
        # Function to perform BFS and find shortest path from city 0 to city n-1
        def bfs():
            queue = deque([0])
            distances = {i: float('inf') for i in range(n)}
            distances[0] = 0
            
            while queue:
                current = queue.popleft()
                
                for neighbor in graph[current]:
                    if distances[neighbor] == float('inf'):  # Not visited
                        distances[neighbor] = distances[current] + 1
                        queue.append(neighbor)
            
            return distances[n - 1] if distances[n - 1] != float('inf') else -1
        
        # Process each query
        for u, v in queries:
            graph[u].append(v)  # Add the new road
            shortest_path_length = bfs()  # Find shortest path after adding the road
            results.append(shortest_path_length)
        
        return results
