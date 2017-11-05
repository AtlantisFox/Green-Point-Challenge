import time
class Solution(object):
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())
        ans = len(nums)

        for x in nums:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
