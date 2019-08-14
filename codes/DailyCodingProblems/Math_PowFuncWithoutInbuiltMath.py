'''Fast Python solution for - 
Implement pow(x, n), which calculates x raised to the power n (xn). Without using Math function '''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
        
        if n == 0:
            return 1
        if n == 1:
            return x
        
        
        if abs(n)%2 == 0:
            y = self.myPow(x,abs(n)/2)
            return y*y
        else:
            y = self.myPow(x,(abs(n)-1)/2)
            return y*y*x

