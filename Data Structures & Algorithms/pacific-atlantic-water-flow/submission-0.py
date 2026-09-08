class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()
        
        # DFS function to explore reachable cells
        def explore(r, c, visited, prev_height):
            in_bounds_row = 0 <= r < rows
            in_bounds_col = 0 <= c < cols

            if not in_bounds_row or not in_bounds_col:
                return

            if (r, c) in visited:
                return

            if heights[r][c] < prev_height:
                return

            visited.add((r, c))

            # Explore in four directions
            explore(r - 1, c, visited, heights[r][c])  # Up
            explore(r + 1, c, visited, heights[r][c])  # Down
            explore(r, c - 1, visited, heights[r][c])  # Left
            explore(r, c + 1, visited, heights[r][c])  # Right

        # Perform DFS from the Pacific and Atlantic borders
        for col in range(cols):
            explore(0, col, pacific_reachable, heights[0][col])  # Top border (Pacific)
            explore(rows - 1, col, atlantic_reachable, heights[rows - 1][col])  # Bottom border (Atlantic)

        for row in range(rows):
            explore(row, 0, pacific_reachable, heights[row][0])  # Left border (Pacific)
            explore(row, cols - 1, atlantic_reachable, heights[row][cols - 1])  # Right border (Atlantic)

        # Intersection of the two sets gives cells that can reach both oceans
        result = list(pacific_reachable & atlantic_reachable)
        return result    