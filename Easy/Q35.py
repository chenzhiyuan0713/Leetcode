"""
1534. 统计好三元组
给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。

如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
其中 |x| 表示 x 的绝对值。

返回 好三元组的数量 。

示例 1：

输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
示例 2：

输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。

"""


class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        result_counter = 0
        for index in range(len(arr)):
            counter = 1
            while index+counter < len(arr):
                if abs(arr[index] - arr[index + counter]) <= a:
                    # print(arr[index], arr[index + counter])
                    counter_2 = 1
                    # counter += 1
                    counter_3 = 0
                    while index + counter + counter_2 < len(arr):
                        if abs(arr[index + counter] - arr[index + counter + counter_2]) <= b:
                            # print(arr[index + counter], arr[index + counter + counter_2])
                            # counter_2 += 1
                            while index + counter + counter_2 + counter_3 < len(arr):
                                if abs(arr[index] - arr[index + counter + counter_2 + counter_3]) <= c:
                                    # print(arr[index + counter + counter_2], arr[index + counter + counter_2 + counter_3])
                                    result_counter += 1
                                    print(arr[index], arr[index + counter], arr[index + counter + counter_2 + counter_3],(index, index + counter, index + counter + counter_2 + counter_3))
                                    counter_3 += 1
                                else:
                                    # print(arr[index],arr[index + counter + counter_2], arr[index + counter + counter_2 + counter_3])
                                    counter_3 += 1
                            counter_2 += 1
                        else:
                            counter_2 += 1
                    counter += 1
                else:
                    counter += 1
        return result_counter


answer = Solution()
# print(answer.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
# print(answer.countGoodTriplets([1,1,2,2,3], 0, 0, 1))
print(answer.countGoodTriplets([4,4,4,0,0,10,7,8,8], 8, 4, 6))
