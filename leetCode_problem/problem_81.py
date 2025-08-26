class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1
        while len(result) < m * n:
            result.append(mat[row][col])
            if direction == 1:
                if col + 1 < n and row - 1 >= 0:
                    row -= 1
                    col += 1
                elif col + 1 < n:
                    col += 1
                    direction = -1
                else:
                    row += 1
                    direction = -1
            else:
                if row + 1 < m and col - 1 >= 0:
                    row += 1
                    col -= 1
                elif row + 1 < m:
                    row += 1
                    direction = 1
                else:
                    col += 1
                    direction = 1
        return result