class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_rows,len_cols = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        islands = 0
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            grid[row][col] = "0"

            while q:
                r, c = q.pop()
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc

                    if (nr<0 or nc<0 or nr>=len_rows or nc>=len_cols or grid[nr][nc] == "0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        for r_g in range(len_rows):
            for c_g in range(len_cols):
                if grid[r_g][c_g] == "1":
                    bfs(r_g,c_g)
                    islands +=1
        return islands
