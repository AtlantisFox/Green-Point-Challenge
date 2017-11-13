class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return True
        maxstep = nums[0]
        for i in range(1,len(nums)):
            if maxstep > 0:
                maxstep -= 1
                maxstep = max(nums[i],maxstep)
            else:
                return False
        return True