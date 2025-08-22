class Solution:
    def minimumArea(self, grid):
        m, n = len(grid), len(grid[0])
        top, left, bottom, right = m, n, -1, -1
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    if i < top: top = i
                    if j < left: left = j
                    if i > bottom: bottom = i
                    if j > right: right = j
        if bottom == -1:
            return 0
        return (bottom - top + 1) * (right - left + 1)
