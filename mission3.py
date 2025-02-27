import heapq
class Solution(object):
    def mission3(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows,cols = len(grid), len(grid[0])
        
        #pq to store current cost, row , col
        pq = [(0,0,0)]
        
        movements = [(0,1),(0,-1),(1,0),(-1,0)]
        effort = [[float('inf')]*cols for _ in range(rows)]
        effort[0][0] = 0
        while pq:
            
            cost,r,c = heapq.heappop(pq)
            if (r,c) == (rows-1,cols-1):
                return cost 
            
            if cost > effort[r][c]:
                continue
            
            for row,col in movements:
                c_row = r+row 
                c_col = c+col
                if 0<= c_row < rows and 0<=c_col < cols:
                    step_cost = abs(grid[c_row][c_col]-grid[r][c])
                    n_cost = max(step_cost,cost)
                    
                    if n_cost < effort[c_row][c_col]:
                        effort[c_row][c_col] = n_cost
                        heapq.heappush(pq,(n_cost, c_row,c_col))
                    
                                      
            
        
        
        
        return -1