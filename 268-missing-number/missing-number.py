class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len(nums)
        l1=sorted(nums)
        add=sum(nums)
        add1=(x*(x+1))//2 #sum of first n natural no.s

        if add==add1:
            if 0 in l1:
                return l1[x-1]+1
            else:
                return 0
        else:
            return add1-add

