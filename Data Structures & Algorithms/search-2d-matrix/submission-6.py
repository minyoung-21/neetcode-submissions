class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        d = len(matrix) - 1

        while t <= d:
            m = t + (d - t) // 2
            l = 0
            r = len(matrix[m]) - 1
            if target >= matrix[m][l] and target <= matrix[m][r]:
                # target might be here
                
                while l <= r:
                    med = l + (r - l) // 2
                    if matrix[m][med] > target:
                        r = med - 1
                    elif matrix[m][med] < target:
                        l = med + 1
                    else:
                        return True
                return False
            elif target < matrix[m][l]:
                # target is in the upper array
                d = m - 1
            elif target > matrix[m][r]:
                # target is in the lower array
                t = m + 1
            
        
        return False