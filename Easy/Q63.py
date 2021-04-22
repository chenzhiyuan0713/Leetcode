"""
1207. 独一无二的出现次数
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。


示例 1：

输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
示例 2：

输入：arr = [1,2]
输出：false
示例 3：

输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true

"""


class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        single_element = []
        counter = []
        if len(arr) == 1:
            return True
        else:
            for each in arr:
                if each not in single_element:
                    single_element.append(each)
            for each_element in single_element:
                counter.append(arr.count(each_element))
            for index in range(len(counter)):
                if counter[index] in counter[index+1:]:
                    return False
            return True
        # return counter


answer = Solution()
print(answer.uniqueOccurrences([1,2,2,1,1,3]))