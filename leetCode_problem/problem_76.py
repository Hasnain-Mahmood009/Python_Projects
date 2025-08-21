class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        height = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1

            stack = []
            sum_row = 0
            for j in range(n):
                count = 1
                while stack and stack[-1][0] >= height[j]:
                    h, c = stack.pop()
                    sum_row -= h * c
                    count += c
                sum_row += height[j] * count
                ans += sum_row
                stack.append((height[j], count))

        return ans
