class Solution:  
    # @return an integer  
    def divide(self, dividend, divisor):  
        sign = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)  
        a, b = abs(dividend), abs(divisor)  
        ret, c = 0, 0  
  
        while a >= b:  
            c = b  
            i = 0  
            while a >= c:  
                a -= c  
                ret += (1<<i)  
                i += 1  
                c <<= 1  
  
        if sign:  
            ret = -ret  
        return min(max(-2147483648, ret), 2147483647)