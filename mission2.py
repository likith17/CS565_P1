from collections import deque
class Solution(object):
    def mission2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        start = (0,0)
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([start])
        end = (rows-1,cols-1)
        visited=[start]
        path = 1
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                if (row,col) == end:
                    return path
                movements = [(row+1,col),(row+1,col+1),(row,col+1),(row,col-1),(row-1,col),(row-1,col-1),(row+1,col-1),(row-1,col+1)]
                for r,c in movements:
                    if (r,c) not in visited and 0<=r<rows and 0<=c<cols and grid[r][c]==0:
                        visited.append((r,c))
                        queue.append((r,c))
            
            path+=1
            
        if path == 1: return "Alert!!!"
            
            
     