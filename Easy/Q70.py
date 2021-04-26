"""
面试题 01.01. 判定字符是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        char_list = []
        for each_char in astr:
            if each_char not in char_list:
                char_list.append(each_char)
            else:
                return False
        return True


answer = Solution()
print(answer.isUnique(""))


