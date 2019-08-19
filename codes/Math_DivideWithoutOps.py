'''Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        q = 0
        sign = +1
        
        if divisor < 0 and dividend <0:
            divisor = divisor * (-1)
            dividend = dividend * (-1)
        elif divisor < 0:
            divisor = divisor * (-1)
            sign = -1
        elif dividend < 0:
            dividend = dividend * (-1)
            sign = -1
                
        if divisor ==1:
            return dividend*sign
            
        reach_no = 0
        while reach_no < dividend:
            q += 1
            reach_no += divisor
            #dividend -= divisor
            
        if reach_no > dividend:
            q -= 1
        return q*sign


a = Solution()
print(a.divide(-2147483648,-1))