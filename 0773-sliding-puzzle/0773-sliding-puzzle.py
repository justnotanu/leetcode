class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert the board to a string for easier comparison
        start_state = ''.join(str(num) for row in board for num in row)
        target_state = '123450'
        
        # Directions for moving the empty space
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Function to find the position of zero
        def find_zero(state):
            return state.index('0')
        
        # BFS setup
        queue = deque([(start_state, find_zero(start_state), 0)])  # (current_state, zero_index, moves)
        visited = {start_state}
        
        while queue:
            current_state, zero_index, moves = queue.popleft()
            
            # Check if we reached the target state
            if current_state == target_state:
                return moves
            
            # Get row and column of zero
            row, col = divmod(zero_index, 3)
            
            # Try all possible moves
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check boundaries
                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new_zero_index = new_row * 3 + new_col
                    
                    # Create new state by swapping zero with adjacent number
                    new_state_list = list(current_state)
                    new_state_list[zero_index], new_state_list[new_zero_index] = new_state_list[new_zero_index], new_state_list[zero_index]
                    new_state = ''.join(new_state_list)
                    
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, new_zero_index, moves + 1))
        
        return -1  # If we exhaust all options and don't reach the target
        