class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        num1=abs(num)
        s=""
        while(num1!=0):
            r=num1%7
            s+=str(r)
            num1//=7
        res=s[::-1]
        if num<0:
            return "-"+res
        else:
            return res

        