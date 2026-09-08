class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        spiral_print = []
        while left < right and top < bottom:
            for num in range(left,right):
                spiral_print.append(matrix[top][num])
            top += 1
            for num in range(top,bottom):
                spiral_print.append(matrix[num][right-1])
            right -= 1    
            if not (left<right and top<bottom):
                break
            for num in range(right-1,left-1,-1):
                spiral_print.append(matrix[bottom-1][num])          
            bottom -= 1
            for num in range(bottom-1, top-1, -1):
                spiral_print.append(matrix[num][left])        
            left += 1

        return spiral_print    
        