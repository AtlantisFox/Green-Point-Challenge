class Solution:
    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        res = 1
        while n > 0:
            if n % 2==1:
                res = ans * a % b
            a = a * a % b
            n = n / 2
        return res % b