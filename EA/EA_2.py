"""
1886. 判断矩阵经轮转后是否一致
给你两个大小为 n x n 的二进制矩阵 mat 和 target 。现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。



示例 1：


输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
输出：true
解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
示例 2：


输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
输出：false
解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
示例 3：


输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
输出：true
解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。


提示：

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] 和 target[i][j] 不是 0 就是 1

"""
from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True

        matrix_length = len(mat)
        if matrix_length == 1:
            return mat == target
        else:
            def rotate_once(input_mat):
                def zhuanzhi(input_list: list) -> list:
                    result = [[each] for each in input_list]
                    return result

                after_process = []
                for col in input_mat:
                    after_process.append(zhuanzhi(col))

                turn_complete = []
                for index in range(matrix_length):
                    new_col = [each_col[index][0] for each_col in after_process]
                    turn_complete.append(new_col[::-1])

                return turn_complete, turn_complete == target

            # rotate three times
            if rotate_once(mat)[1]:
                return True
            elif rotate_once(rotate_once(mat)[0])[1]:
                return True
            elif rotate_once(rotate_once(rotate_once(mat)[0])[0])[1]:
                return True
            else:
                return False


answer = Solution()
print(answer.findRotation(mat = [[0,0,0],[0,0,1],[0,0,1]], target = [[0,0,0],[0,0,1],[0,0,1]]))
