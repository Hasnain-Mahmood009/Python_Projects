import math
from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = m * n
        ans = INF

        def minimumArea(si, ei, sj, ej) -> int:
            x1 = y1 = math.inf
            x2 = y2 = -math.inf
            for i in range(si, ei + 1):
                for j in range(sj, ej + 1):
                    if grid[i][j] == 1:
                        x1 = min(x1, i)
                        y1 = min(y1, j)
                        x2 = max(x2, i)
                        y2 = max(y2, j)
            return 0 if x1 == math.inf else (x2 - x1 + 1) * (y2 - y1 + 1)

        for i in range(m):
            top = minimumArea(0, i, 0, n - 1)
            for j in range(n):
                area = top + minimumArea(i + 1, m - 1, 0, j) + minimumArea(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, area)

        for i in range(m):
            bottom = minimumArea(i, m - 1, 0, n - 1)
            for j in range(n):
                area = bottom + minimumArea(0, i - 1, 0, j) + minimumArea(0, i - 1, j + 1, n - 1)
                ans = min(ans, area)

        for j in range(n):
            left = minimumArea(0, m - 1, 0, j)
            for i in range(m):
                area = left + minimumArea(0, i, j + 1, n - 1) + minimumArea(i + 1, m - 1, j + 1, n - 1)
                ans = min(ans, area)

        for j in range(n):
            right = minimumArea(0, m - 1, j, n - 1)
            for i in range(m):
                area = right + minimumArea(0, i, 0, j - 1) + minimumArea(i + 1, m - 1, 0, j - 1)
                ans = min(ans, area)

        for i1 in range(m):
            for i2 in range(i1 + 1, m):
                area = minimumArea(0, i1, 0, n - 1) + minimumArea(i1 + 1, i2, 0, n - 1) + minimumArea(i2 + 1, m - 1, 0, n - 1)
                ans = min(ans, area)

        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                area = minimumArea(0, m - 1, 0, j1) + minimumArea(0, m - 1, j1 + 1, j2) + minimumArea(0, m - 1, j2 + 1, n - 1)
                ans = min(ans, area)

        return ans
