import heapq

class Solution(object):
    def mission4(self, grid):
        
        if not self.is_solvable(grid):
            return "Alert!!!"  # Unsolvable case

        target = tuple(tuple(row) for row in [[1, 2, 3], [4, 5, 0]])  # Target grid as tuple
        start = tuple(tuple(row) for row in grid)  
        rows, cols = 2, 3  
        
        # Locate empty spot (0)
        empty_pos = next((r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0)
        
        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        # Priority queue which holds f(n), g(n), state, empty_pos
        queue = [(self.heuristic(grid), 0, start, empty_pos)]
        visited = set()
        visited.add(start)

        while queue:
          
            _, moves, state, (zero_r, zero_c) = heapq.heappop(queue)

            # If target reached, 
            if state == target:
                return moves

            # Try all possible movements
            for row, col in movements:
                n_row, n_col = zero_r + row, zero_c + col
                if 0 <= n_row < rows and 0 <= n_col < cols:  
                    new_state = [list(row) for row in state]  
                    new_state[zero_r][zero_c], new_state[n_row][n_col] = new_state[n_row][n_col], new_state[zero_r][zero_c]
                    new_tuple_state = tuple(tuple(row) for row in new_state)  

                    if new_tuple_state not in visited:
                        visited.add(new_tuple_state)
                        heapq.heappush(queue, (moves + 1 + self.heuristic(new_state), moves + 1, new_tuple_state, (n_row, n_col)))

        return "Alert!!!"  # no solution is found

    def heuristic(self, state):
        
        target_positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 0: (1, 2)
        }
        distance = 0
        for r in range(2):
            for c in range(3):
                tile = state[r][c]
                target_r, target_c = target_positions[tile]
                distance += abs(r - target_r) + abs(c - target_c)
        return distance

    def count_inversions(self, grid):
        flattened = [num for row in grid for num in row if num != 0]  # Flatten grid & remove 0
        inversions = 0
        for i in range(len(flattened)):
            for j in range(i + 1, len(flattened)):
                if flattened[i] > flattened[j]:  # Count inversion
                    inversions += 1
        return inversions

    def is_solvable(self, grid):
        return self.count_inversions(grid) % 2 == 0
