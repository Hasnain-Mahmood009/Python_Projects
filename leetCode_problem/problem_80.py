import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = 0
        max_area = 0
        
        for l, w in dimensions:
            diag = math.sqrt(l*l + w*w)
            area = l * w
            
            if diag > max_diag or (diag == max_diag and area > max_area):
                max_diag = diag
                max_area = area
                
        return max_area
