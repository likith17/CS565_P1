class Solution(object):
    def mission1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
     
        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            # Mark battleship as visited by sinking it.
            grid[r][c] = "0"
            # battleships are connected horizontally and vertically.
            movements = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
           
            for row, col in movements:
                if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                    dfs(row, col)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1   # Found a new battleship cluster.
                    dfs(i, j)    # Use DFS with movement list to "sink" the entire cluster.   
        return count
  