class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        m, n = len(matrix), len(matrix[0])

        firstRow, lastRow = 0, m-1
        while firstRow <= lastRow:#log m
            mid = (firstRow + lastRow ) // 2
            if target > matrix[mid][-1]:
                firstRow = mid + 1
            elif target < matrix[mid][0]:
                lastRow = mid - 1
            else:
                break
        if not (firstRow <= lastRow):
            return False 
        row = (firstRow + lastRow)//2    
        l, r = 0, n-1
        
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
