class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x%2 == 0:
            for i in range(2,x+1,2):
                y = i * i
                if y == x:
                    return i
                elif y > x:
                    return i - 2
        else:
            for i in range(0,x+1,2):
                y = i * i
                if y == x:
                    return i
                elif y > x:
                    return i - 2