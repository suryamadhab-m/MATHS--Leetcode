class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1
        ans = False
        while i <= n:
            if i == n:
                ans = True
                break
            i *= 3
        return ans