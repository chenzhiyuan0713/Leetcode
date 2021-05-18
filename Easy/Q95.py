"""
463. 岛屿的周长
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。

网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。



示例 1：



输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
示例 2：

输入：grid = [[1]]
输出：4
示例 3：

输入：grid = [[1,0]]
输出：4


提示：

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] 为 0 或 1

"""
from typing import List


class Solution2:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid)-1
        counter = 0
        if length == 1:
            if grid[0][0] == 1:
                return 4
            else:
                return 0
        for i in range(length):
            if i == 0:
                for j in range(length):
                    if j == 0:
                        if grid[i][j] == 1:
                            counter += 1
                        if grid[i + 1][j] == 0 and grid[i][j] == 1:
                            counter += 1
                        if grid[i][j + 1] == 0 and grid[i][j] == 1:
                            counter += 1
                        continue
                    if j == length:
                        if grid[i][j] == 1:
                            counter += 1
                        if grid[i - 1][j] == 0 and grid[i][j] == 1:
                            counter += 1
                        if grid[i][j - 1] == 0 and grid[i][j] == 1:
                            counter += 1
                        continue

                    if grid[i][j] == 1:
                        counter += 1
                    if grid[i - 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j - 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j + 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    continue

            if i == length:
                for j in range(length):
                    if j == 0:
                        if grid[i][j] == 1:
                            counter += 1
                        if grid[i - 1][j] == 0 and grid[i][j] == 1:
                            counter += 1
                        if grid[i][j + 1] == 0 and grid[i][j] == 1:
                            counter += 1
                        continue
                    if j == length:
                        if grid[i][j] == 1:
                            counter += 1
                        if grid[i - 1][j] == 0 and grid[i][j] == 1:
                            counter += 1
                        if grid[i][j - 1] == 0 and grid[i][j] == 1:
                            counter += 1
                        continue

                    if grid[i][j] == 1:
                        counter += 1
                    if grid[i - 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j - 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j + 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    continue

            for j in range(length):
                if j == 0:
                    if grid[i][j] == 1:
                        counter += 1
                    if grid[i - 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i + 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j + 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    continue
                if j == length:
                    if grid[i][j] == 1:
                        counter += 1
                    if grid[i - 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i + 1][j] == 0 and grid[i][j] == 1:
                        counter += 1
                    if grid[i][j - 1] == 0 and grid[i][j] == 1:
                        counter += 1
                    continue

                if grid[i-1][j] == 0 and grid[i][j] == 1:
                    counter += 1
                if grid[i+1][j] == 0 and grid[i][j] == 1:
                    counter += 1
                if grid[i][j-1] == 0 and grid[i][j] == 1:
                    counter += 1
                if grid[i][j+1] == 0 and grid[i][j] == 1:
                    counter += 1

        return counter


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length = len(grid)
        length_y = len(grid[0])
        counter = 0
        # if length == 1:
        #     if grid[0][0] == 1:
        #         return 4
        #     else:
        #         return 0
        for i in range(length):
            for j in range(length_y):
                if grid[i][j] == 1:
                    counter += 4
        for i in range(length):
            if i == 0:
                for j in range(length):
                    if j == 0:
                        if grid[i + 1][j] == 1 and grid[i][j] == 1:
                            counter -= 1
                        if grid[i][j + 1] == 1 and grid[i][j] == 1:
                            counter -= 1
                        continue
                    if j == length - 1:
                        if grid[i + 1][j] == 1 and grid[i][j] == 1:
                            counter -= 1
                        if grid[i][j - 1] == 1 and grid[i][j] == 1:
                            counter -= 1
                        continue

                    if grid[i + 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j - 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j + 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                continue

            if i == length-1:
                for j in range(length):
                    if j == 0:
                        if grid[i - 1][j] == 1 and grid[i][j] == 1:
                            counter -= 1
                        if grid[i][j + 1] == 1 and grid[i][j] == 1:
                            counter -= 1
                        continue
                    if j == length - 1:
                        if grid[i - 1][j] == 1 and grid[i][j] == 1:
                            counter -= 1
                        if grid[i][j - 1] == 1 and grid[i][j] == 1:
                            counter -= 1
                        continue

                    if grid[i - 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j - 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j + 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                continue

            for j in range(length):
                if j == 0:
                    if grid[i - 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i + 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j + 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                    continue
                if j == length-1:
                    if grid[i - 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i + 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                    if grid[i][j - 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                    continue

                if grid[i - 1][j] == 1 and grid[i][j] == 1:
                    counter -= 1
                if grid[i + 1][j] == 1 and grid[i][j] == 1:
                    counter -= 1
                if grid[i][j - 1] == 1 and grid[i][j] == 1:
                    counter -= 1
                if grid[i][j + 1] == 1 and grid[i][j] == 1:
                    counter -= 1
        return counter


class Solution3:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        length_x = len(grid)
        length_y = len(grid[0])
        counter = 0
        for i in range(length_x):
            for j in range(length_y):
                if grid[i][j] == 1:
                    counter += 4
        for i in range(length_x):
            for j in range(length_y):
                try:
                    if grid[i - 1][j] == 1 and grid[i][j] == 1 and i-1 >= 0:
                        counter -= 1
                except:
                    pass
                try:
                    if grid[i + 1][j] == 1 and grid[i][j] == 1:
                        counter -= 1
                except:
                    pass
                try:
                    if grid[i][j - 1] == 1 and grid[i][j] == 1 and j-1 >= 0:
                        counter -= 1
                except:
                    pass
                try:
                    if grid[i][j + 1] == 1 and grid[i][j] == 1:
                        counter -= 1
                except:
                    pass

        return counter


answer = Solution3()
print(answer.islandPerimeter([[1,0]]))
