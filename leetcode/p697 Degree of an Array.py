import time


'''
    log(n)
'''

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



'''
这是刚开始写的 log(n^2) 的
'''
# class Solution(object):
#
#     def calc_range(self, nums, num):
#         length = len(nums)
#         left = 0
#         right = length - 1
#
#         for i in range(length):
#             if nums[i] == num:
#                 left = i
#                 break
#         for i in range(length - 1, -1, -1):
#             if nums[i] == num:
#                 right = i
#                 break
#
#         return right - left + 1
#
#     def findShortestSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if nums == []:
#             return 0
#
#         f = {}
#         for i in nums:
#             if f.get(i) == None:
#                 f[i] = 1
#             else:
#                 f[i] += 1
#
#         max_value = -1
#         for key, value in f.items():
#             if value > max_value:
#                 max_value = value
#
#         if max_value == 1:
#             return 1
#
#         todo_list = []
#
#         for key, value in f.items():
#             if value == max_value:
#                 todo_list.append(key)
#
#         ans = 50001
#
#         for i in todo_list:
#             if self.calc_range(nums, i) < ans:
#                 ans = self.calc_range(nums, i)
#
#         return ans


if __name__ == '__main__':
    start = time.time()

    a = Solution()
    nums = [1,2,2,3,1,4,2]
    print(a.findShortestSubArray(nums))

    end = time.time()

    print(end - start)