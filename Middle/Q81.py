'''
剑指 Offer 56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。



示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1


限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31

'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_list = []
        del_list = []
        for each in nums:
            if each not in num_list and each not in del_list:
                num_list.append(each)
            elif each in num_list:
                num_list.remove(each)
                del_list.append(each)
        return num_list[0]


answer = Solution()
print(answer.singleNumber([3]))
