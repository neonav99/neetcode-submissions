class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows , num_cols = len(matrix), len(matrix[0])

        l, r = 0, num_rows*num_cols - 1

        while l <= r:
            mid = l + (r-l)//2
            row = mid//num_cols
            col = mid%num_cols
            if target == matrix[row][col]:
                return True
            if target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False

