"""
1725. 可以形成最大正方形的矩形数目
给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。

如果存在 k 同时满足 k <= li 和 k <= wi ，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 4 的正方形。

设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。

返回可以切出边长为 maxLen 的正方形的矩形 数目 。



示例 1：

输入：rectangles = [[5,8],[3,9],[5,12],[16,5]]
输出：3
解释：能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
最大正方形的边长为 5 ，可以由 3 个矩形切分得到。
示例 2：

输入：rectangles = [[2,3],[3,7],[4,3],[3,7]]
输出：3

"""


class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        rectangles_result = []
        for one_rec in rectangles:
            rectangles_result.append(min(one_rec))
        max_length = max(rectangles_result)
        counter = 0
        for single_result in rectangles_result:
            if max_length == single_result:
                counter += 1
        return counter


answer = Solution()
print(answer.countGoodRectangles([[5,8],[3,9],[5,12],[16,5]]))

"""
执行用时：
52 ms
, 在所有 Python3 提交中击败了
75.69%
的用户
内存消耗：
14.7 MB
, 在所有 Python3 提交中击败了
99.54%
的用户
"""