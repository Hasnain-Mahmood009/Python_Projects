from itertools import permutations
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in [nums[i] + nums[j], nums[i] - nums[j], nums[j] - nums[i],
                                   nums[i] * nums[j]]:
                            if solve(next_nums + [op]):
                                return True
                        if abs(nums[j]) > 1e-6 and solve(next_nums + [nums[i] / nums[j]]):
                            return True
                        if abs(nums[i]) > 1e-6 and solve(next_nums + [nums[j] / nums[i]]):
                            return True
            return False
        for perm in permutations(cards):
            if solve(list(perm)):
                return True
        return False
