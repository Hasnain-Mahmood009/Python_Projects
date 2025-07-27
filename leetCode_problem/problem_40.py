class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        formula = len(nums) / 2
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for key in count:
            if count[key] > formula:
                return key