"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。



示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 20

1  2  3  4
12 13 14 5
11 16 15 6
10 9  8  7

1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""
from typing import List


# 思路： 除了第一行n个， 两个 n-1 两个 n-2 直到 min = 1
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # all_nums = [i+1 for i in range(n**2)]
        start = 1
        count_two = 2
        # max length : n
        max_length = n
        left, right, up, down = 0, n-1, 0, n-1
        result = [[0 for i in range(n)] for j in range(n)]
        range_list = [i for i in range(n)]
        while start <= n ** 2:

        return result


answer = Solution()
print(answer.generateMatrix(3))
