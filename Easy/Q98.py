"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cache = [[0, 1]]
        final_result = []
        for i in range(numRows):
            each_line = []
            for each in range(i+1):
                if each == i:
                    each_line.append(cache[i][-1])
                    final_result.append(each_line[:])
                    each_line.insert(0, 0)
                    cache.append(each_line)
                else:
                    each_line.append(cache[i][each] + cache[i][each+1])

        return final_result


answer = Solution()
print(answer.generate(10))
