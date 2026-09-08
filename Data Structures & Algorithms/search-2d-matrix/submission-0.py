class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_p_row, right_p_row = 0, len(matrix) - 1

        while left_p_row<=right_p_row:
            mid_row = left_p_row + (right_p_row-left_p_row) // 2
            left_p_col, right_p_col = 0, len(matrix[0]) - 1
            while left_p_col<=right_p_col:
                mid_col = left_p_col + (right_p_col - left_p_col) // 2
                if matrix[mid_row][mid_col] == target:
                    return True
                if matrix[mid_row][mid_col] > target:
                    right_p_row = mid_row - 1
                    right_p_col = mid_col - 1
                else:
                    left_p_row = mid_row + 1
                    left_p_col = mid_col + 1
        return False

