class Solution:
    def maxCollectedFruits(self, grid):
        size = len(grid)
        diagonal_sum = 0

        for idx, line in enumerate(grid):
            diagonal_sum += line[idx]

        for row in range(size - 2):
            grid[row][size - 2 - row] = 0
            grid[row][size - 3 - row] = 0
        grid[size - 2][0] = 0

        for r in range(1, size - 1):
            for c in range(max(r + 1, size - r - 1), size - 1):
                grid[r][c] += max(grid[r - 1][c - 1], grid[r - 1][c], grid[r - 1][c + 1])
            grid[r][-1] += max(grid[r - 1][-2], grid[r - 1][-1])

        for c in range(1, size - 1):
            for r in range(max(c + 1, size - c - 1), size - 1):
                grid[r][c] += max(grid[r - 1][c - 1], grid[r][c - 1], grid[r + 1][c - 1])
            grid[-1][c] += max(grid[-2][c - 1], grid[-1][c - 1])

        return diagonal_sum + grid[size - 2][size - 1] + grid[size - 1][size - 2]
