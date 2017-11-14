# -*- coding:utf-8 -*-
class Solution(object):

    """docstring for Solution"""

    def __init__(self, arg):
        super(Solution, self).__init__()
        self.arg = arg

    def next_permutation(a):
        if len(num) < 2:
            return num
        partition = -1
        for i in range(len(num) - 2, -1, -1):
            if num[i] < num[i + 1]:
                partition = i
                break
        if partition == -1:
            return num[::-1]
        for i in range(len(num) - 1, partition, -1):
            if num[i] > num[partition]:
                num[i], num[partition] = num[partition], num[i]
                break
        num[partition + 1:] = num[partition + 1:][::-1]
        return num
