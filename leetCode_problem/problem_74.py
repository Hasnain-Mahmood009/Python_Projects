class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        total_subarrays = 0
        current_consecutive_zeros = 0
        for num in nums:
            if num == 0:
                current_consecutive_zeros += 1
            else:
                total_subarrays += (current_consecutive_zeros * (current_consecutive_zeros + 1)) // 2
                current_consecutive_zeros = 0
        total_subarrays += (current_consecutive_zeros * (current_consecutive_zeros + 1)) // 2
        return total_subarrays