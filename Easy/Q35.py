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


# class Solution:
#     def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
#         result_counter = 0
#         for index in range(len(arr)):
#             counter = 1
#             while index+counter < len(arr):
#                 if abs(arr[index] - arr[index + counter]) <= a:
#                     # print(arr[index], arr[index + counter])
#                     counter_2 = 1
#                     # counter += 1
#                     counter_3 = 0
#                     while index + counter + counter_2 < len(arr):
#                         if abs(arr[index + counter] - arr[index + counter + counter_2]) <= b:
#                             # print(arr[index + counter], arr[index + counter + counter_2])
#                             # counter_2 += 1
#                             while index + counter + counter_2 + counter_3 < len(arr):
#                                 if abs(arr[index] - arr[index + counter + counter_2 + counter_3]) <= c and abs(arr[index] - arr[index + counter + counter_2 + counter_3]) <= b:
#                                     # print(arr[index + counter + counter_2], arr[index + counter + counter_2 + counter_3])
#                                     result_counter += 1
#                                     print(arr[index], arr[index + counter], arr[index + counter + counter_2 + counter_3],(index, index + counter, index + counter + counter_2 + counter_3))
#                                     counter_3 += 1
#                                 else:
#                                     # print(arr[index],arr[index + counter + counter_2], arr[index + counter + counter_2 + counter_3])
#                                     break
#                             counter_2 += 1
#                         else:
#                             counter_2 += 1
#                     counter += 1
#                 else:
#                     counter += 1
#         return result_counter



class Solution2:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0
        for index_i in range(n-2):
            for index_j in range(index_i + 1, n-1):
                if abs(arr[index_i] - arr[index_j]) <= a:
                    for index_k in range(index_j + 1, n):
                        if abs(arr[index_j] - arr[index_k]) <= b and abs(arr[index_i] - arr[index_k]) <= c:
                            result += 1
        return result


answer = Solution2()
# print(answer.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3))
# print(answer.countGoodTriplets([1,1,2,2,3], 0, 0, 1))
# print(answer.countGoodTriplets([4,4,4,0,0,10,7,8,8], 8, 4, 6))
# print(answer.countGoodTriplets([2,6,9,0,1,8], 3, 1, 2))

#
# 0 1 2
# 0 1 3
# 0 1 4
# 0 1 6
# 0 1 7
# 0 1 8
# 0 2 3
# 0 2 4
# 0 2 6
# 0 2 7
# 0 2 8
# 0 3 4
# 0 5 6
# 0 5 7
# 0 5 8
# 0 6 7
# 0 6 8
# 0 7 8
# 1 2 3
# 1 2 4
# 1 2 6
# 1 2 7
# 1 2 8
# 1 3 4
# 1 5 6
# 1 5 7
# 1 5 8
# 1 6 7
# 1 6 8
# 1 7 8
# 2 3 4
# 2 5 6
# 2 5 7
# 2 5 8
# 2 6 7
# 2 6 8
# 2 7 8
# 5 6 7
# 5 6 8
# 5 7 8
# 6 7 8
# 41
