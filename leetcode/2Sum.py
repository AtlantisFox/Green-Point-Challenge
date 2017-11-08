# -*- coding: utf-8 -*-

class Solution:
    def twosum(self,nums,target):
        a = {}
        for i in range(len(nums)):
            if target-nums[i] in a:
                return (a[target- nums[i]]+1,i+1)
            a[nums[i]] = i

