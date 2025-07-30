class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0 
        li = []
        while n > 0:
            li.append(n%2)
            n = n // 2
        for i in range(len(li)):
            if li[i] == 1:
                count += 1
        return count