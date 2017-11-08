# -*- coding: utf-8 -*-

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        offset = 0
        while m!=n:
            m = m >> 1
            n = n >> 1
            offset = offset + 1
        return m<<offset
