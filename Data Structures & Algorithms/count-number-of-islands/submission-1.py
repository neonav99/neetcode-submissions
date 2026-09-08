class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if explore(grid,row,col,visited):
                    count+=1
        return count

def explore(grid,row,col,visited):
    in_bound_row = 0<= row < len(grid)
    in_bound_col = 0<= col < len(grid[0])

    if not in_bound_row or not in_bound_col:
        return False

    if grid[row][col] != "1":
        return False

    pos = (row,col)
    if pos in visited:
        return False
    
    visited.add(pos)
    
    explore(grid,row-1,col,visited)
    explore(grid,row+1,col,visited)
    explore(grid,row,col-1,visited)
    explore(grid,row,col+1,visited)

    return True


