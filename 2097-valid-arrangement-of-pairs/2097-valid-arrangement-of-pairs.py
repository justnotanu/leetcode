class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Create a graph representation
        graph = defaultdict(deque)
        for start, end in pairs:
            graph[start].append(end)
        
        # Find the starting point for Eulerian path
        start_point = pairs[0][0]  # Default start point
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)

        for start, end in pairs:
            out_degree[start] += 1
            in_degree[end] += 1
        
        for start in out_degree:
            if out_degree[start] > in_degree[start]:
                start_point = start
                break
        
        # Perform DFS to find the valid arrangement
        result = []
        
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            result.append(node)

        dfs(start_point)
        
        # Reverse the result to get the correct order of pairs
        result.reverse()
        
        # Constructing the final arrangement
        arrangement = []
        for i in range(len(result) - 1):
            arrangement.append([result[i], result[i + 1]])
        
        return arrangement
        