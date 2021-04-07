"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):


        # result = []
        # length = len(nums) - 1
        # if length == 0:
        #     return [nums]
        # else:
        #     for turn in range(length):
        #         length_one_turn = length
        #         while length_one_turn >= 0:
        #             nums[length_one_turn], nums[length_one_turn - 1] = nums[length_one_turn - 1], nums[length_one_turn]
        #             result.append(nums[:])
        #             # 深拷贝的实现
        #             length_one_turn -= 1
        # return result


answer = Solution()
# print(answer.permute([1,2,3]))
print(answer.permute([5, 4, 6, 2]))
print(answer.permute([1, 2, 4]))

a = [[5, 4, 6, 2], [5, 4, 2, 6], [5, 6, 4, 2], [5, 6, 2, 4], [5, 2, 4, 6], [5, 2, 6, 4], [4, 5, 6, 2], [4, 5, 2, 6],
     [4, 6, 5, 2], [4, 6, 2, 5], [4, 2, 5, 6], [4, 2, 6, 5], [6, 5, 4, 2], [6, 5, 2, 4], [6, 4, 5, 2], [6, 4, 2, 5],
     [6, 2, 5, 4], [6, 2, 4, 5], [2, 5, 4, 6], [2, 5, 6, 4], [2, 4, 5, 6], [2, 4, 6, 5], [2, 6, 5, 4], [2, 6, 4, 5]]

