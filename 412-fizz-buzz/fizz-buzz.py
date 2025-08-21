class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l=[]
        for i in range(n):
            x=i+1
            if x%3==0 and x%5==0:
                l.append("FizzBuzz")
            elif x%3==0:
                l.append("Fizz")
            elif x%5==0:
                l.append("Buzz")
            
            else:
                l.append(str(x))
        return l

        