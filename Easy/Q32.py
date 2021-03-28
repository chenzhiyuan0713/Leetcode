"""
461. 汉明距离
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        counter = 0
        x, y = bin(x).replace("b", ""), bin(y).replace("b", "")
        length = max(len(x), len(y))
        if length > len(x):
            x = "0" * (length - len(x)) + x
        if length > len(y):
            y = "0" * (length - len(y)) + y
        x_list = list(x)
        y_list = list(y)
        for i in range(length):
            if x_list[i] != y_list[i]:
                counter += 1
        return counter


answer = Solution()
print(answer.hammingDistance(2, 4))