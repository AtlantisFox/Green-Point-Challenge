# -*- coding:utf-8 -*-

class Solution():
    def __init__(self):
        pass

    def ThreeSum(self, nums):
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        target = 0
        i = 0
        while i < len(nums) - 2:
            p = i + 1
            q = len(nums) - 1
            while p < q:
                if nums[i] + nums[p] + nums[q] > target:
                    q -= 1
                elif nums[i] + nums[p] + nums[q] < target:
                    p += 1
                else:
                    result.append([nums[i], nums[p], nums[q]])
                    q -= 1
                    p += 1
                    while p < q and nums[p] == nums[p - 1]:
                        p += 1
                    while p < q and nums[q] == nums[q + 1]:
                        q -= 1
            while i < len(nums) - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return result