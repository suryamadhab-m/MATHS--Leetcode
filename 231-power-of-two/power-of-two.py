class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(32):
            if(2**i)==n:
                return True
                break
        return False        