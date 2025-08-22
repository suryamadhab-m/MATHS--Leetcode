class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1  # F(0), F(1)
            for _ in range(2, n + 1):  # Loop from F(2) to F(n)
                a, b = b, a + b
            return b