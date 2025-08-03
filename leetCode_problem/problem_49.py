class Solution:
    def maxTotalFruits(self, fruits ,startPos, k):
        left = 0
        total = 0
        max_fruits = 0

        for right in range(len(fruits)):
            total += fruits[right][1]

            while left <= right and min(
                abs(startPos - fruits[left][0]) + abs(fruits[right][0] - fruits[left][0]),
                abs(startPos - fruits[right][0]) + abs(fruits[right][0] - fruits[left][0])
            ) > k:
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits
