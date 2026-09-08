import numpy as np
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        row_len_mat1 = len(mat1)
        col_len_mat1 = len(mat1[0])
        row_len_mat2 = len(mat2)
        col_len_mat2 = len(mat2[0])

        # Check if multiplication is possible
        if col_len_mat1 != row_len_mat2:
            raise ValueError("Matrix multiplication not possible")

        new_mat = np.zeros((row_len_mat1, col_len_mat2), dtype=int)

        for i in range(row_len_mat1):
            for j in range(col_len_mat2):
                for k in range(col_len_mat1):
                    new_mat[i][j] += mat1[i][k] * mat2[k][j]

        return new_mat.tolist()
