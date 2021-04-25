"""
942. 增减字符串匹配
给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]


示例 1：

输入："IDID"
输出：[0,4,1,3,2]
示例 2：

输入："III"
输出：[0,1,2,3]
示例 3：

输入："DDI"
输出：[3,2,0,1]

"""


class Solution:
    def diStringMatch(self, s: str) -> list:
        result = []
        origin = [i for i in range(len(s)+1)]
        for signal in s:
            if signal == "D":
                result.append(max(origin))
                origin.remove(max(origin))
            else:
                result.append(min(origin))
                origin.remove(min(origin))
        result.append(origin[0])
        return result


answer = Solution()
print(answer.diStringMatch("DDI"))
