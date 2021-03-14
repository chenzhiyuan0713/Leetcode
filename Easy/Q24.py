"""
1572. 矩阵对角线元素的和
给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

示例  1：



输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。
示例  2：

输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8
示例 3：

输入：mat = [[5]]
输出：5

"""


class Solution:
    def diagonalSum(self, mat) -> int:
        result = []
        for index in range(0, len(mat[0])):
            result.append(mat[index][index])
            result.append(mat[index][len(mat[0])-1 - index])
        if len(mat[0]) % 2 == 0:
            return sum(result)
        elif len(mat[0]) % 2 != 0 and len(mat[0]) != 1:
            return sum(result) - mat[(len(mat[0])) // 2][(len(mat[0])) // 2]
        else:
            return mat[0][0]


answer = Solution()
print(answer.diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]]))
