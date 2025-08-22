class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        main=0
        for i in nums:
            count=0
            x=i
            while x!=0:
                r=x%10
                count+=1
                x//=10
            if count%2==0:
                main+=1
        return main
        