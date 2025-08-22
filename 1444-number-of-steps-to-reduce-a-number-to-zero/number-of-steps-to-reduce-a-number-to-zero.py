class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        x=num
        count=0
        while(x!=0):
            if x%2==0:
                x//=2
                count+=1
            elif x%2!=0:
                x=x-1
                count+=1
        return count
        