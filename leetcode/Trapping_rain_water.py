class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        secHeight = 0
        left = 0
        right = len(height) - 1
        area = 0
        while (left < right):
            if (height[left] < height[right]):
                secHeight = max(height[left], secHeight)
                area += secHeight - height[left]
                left += 1
            else:
                secHeight = max(height[right], secHeight)
                area += secHeight - height[right]
                right -= 1
        return area