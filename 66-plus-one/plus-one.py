class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=''
        for i in digits:
            s+=str(i)
        x=str(int(s)+1)
        L=[]
        for i in x:
            L.append(int(i))
        return L

        