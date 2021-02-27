'''
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。


示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
'''


class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
    def twoSum(self, nums, target: int):
        nums_1_index = 0
        nums_2_index = 0
        for nums_1 in nums:
            # 这里反复执行了两次，错了一次
            # nums_2_index += 1
            nums_2_index = nums_1_index + 1
            for nums_2 in nums[nums_1_index+1:]:
                if nums_2 + nums_1 == target:
                    return [nums_1_index, nums_2_index]
                else:
                    nums_2_index += 1
            nums_1_index += 1
        return "Not match"


answer_test = Solution()
numssss = [3,2,4]
targetttt = 6
print(answer_test.twoSum(numssss, targetttt))
