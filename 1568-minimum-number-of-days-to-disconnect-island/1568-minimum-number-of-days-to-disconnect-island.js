/**
 * @param {number[][]} grid
 * @return {number}
 */
var minDays = function(grid) {
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const m = grid.length;
    const n = grid[0].length;

    // DFS function to explore the grid
    function dfs(i, j, visited) {
        // Check for out of bounds, already visited, or water (0)
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || grid[i][j] === 0) {
            return;
        }

        visited[i][j] = true; // Mark the cell as visited

        // Explore all four directions
        for (const dir of directions) {
            const new_i = i + dir[0];
            const new_j = j + dir[1];
            dfs(new_i, new_j, visited);
        }
    }

    // Function to count the number of islands
    function countIslands() {
        const visited = Array.from({ length: m }, () => Array(n).fill(false));
        let islands = 0;

        for (let i = 0; i < m; i++) {
            for (let j = 0; j < n; j++) {
                if (!visited[i][j] && grid[i][j] === 1) { // Found an island
                    dfs(i, j, visited);
                    islands++;
                }
            }
        }

        return islands;
    }

    let islands = countIslands();

    // Grid is already disconnected
    if (islands !== 1) {
        return 0;
    }

    // Check if removing a single cell can disconnect the grid
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 1) {
                grid[i][j] = 0; // Temporarily mark the cell as water
                
                const newIslands = countIslands();
                
                grid[i][j] = 1; // Restore the cell back to land
                if (newIslands !== 1) {
                    return 1; // One move is enough to disconnect the grid
                }
            }
        }
    }

    return 2; // It's always possible to break an island with 2 moves
};
