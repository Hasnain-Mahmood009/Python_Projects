class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for index,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return[seen[complement],index]
            seen[num] = index
ts = Solution()
my_list=[1,3,2,6,6]
print(ts.twoSum(my_list,9))