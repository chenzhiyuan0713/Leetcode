"""
给你一个字符串s，请你根据下面的算法重新构造字符串：

从 s中选出 最小的字符，将它 接在结果字符串的后面。
从 s剩余字符中选出最小的字符，且该字符比上一个添加的字符大，将它 接在结果字符串后面。
重复步骤 2 ，直到你没法从 s中选择字符。
从 s中选出 最大的字符，将它 接在结果字符串的后面。
从 s剩余字符中选出最大的字符，且该字符比上一个添加的字符小，将它 接在结果字符串后面。
重复步骤 5，直到你没法从 s中选择字符。
重复步骤 1 到 6 ，直到 s中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将s中字符重新排序后的 结果字符串 。



示例 1：

输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
示例 2：

输入：s = "rat"
输出："art"
解释：单词 "rat" 在上述算法重排序以后变成 "art"
示例 3：

输入：s = "leetcode"
输出："cdelotee"
示例 4：

输入：s = "ggggggg"
输出："ggggggg"
示例 5：

输入：s = "spo"
输出："ops"

"""


class Solution:
    def sortString(self, s: str) -> str:
        ss = list(s)
        new_string = ""
        whole_counter = len(s)

        def min_add(s_example, new_string_example):
            counter = 0
            last_time = " "
            while s_example:
                if last_time == min(s_example):
                    last_time = min(s_example)
                    s_example.remove(min(s_example))
                else:
                    new_string_example += min(s_example)
                    last_time = min(s_example)
                    s_example.remove(min(s_example))
                    counter += 1
            return new_string_example, counter, -1

        def max_add(s_example, new_string_example):
            counter = 0
            last_time = " "
            while s_example:
                if last_time == max(s_example):
                    last_time = max(s_example)
                    s_example.remove(max(s_example))
                else:
                    new_string_example += max(s_example)
                    last_time = max(s_example)
                    s_example.remove(max(s_example))
                    counter += 1
            return new_string_example, counter, 1

        def delete_them(start_string: str, new_string2: str):
            result2 = ""
            start_string_list = list(start_string)
            for each in new_string2:
                start_string_list.remove(each)
            for i in start_string_list:
                result2 += i
            return result2

        turn = 1
        # while whole_counter > 0:
        #     if turn == 1:
        #         new_string, count, turn = min_add(s, new_string)
        #         whole_counter -= count
        #         print(new_string, "min")
        #     elif turn == -1:
        #         new_string, count, turn = max_add(s, new_string)
        #         whole_counter -= count
        #         print(new_string, "max")
        # return new_string
        result = ""
        while whole_counter > 0:
            if turn == 1:
                new_string, count, turn = min_add(ss, new_string)
                whole_counter -= count
                new_string = delete_them(s, new_string)
                result += new_string
                print(new_string, "min")
            elif turn == -1:
                new_string, count, turn = max_add(ss, new_string)
                whole_counter -= count
                new_string = delete_them(s, new_string)
                result += new_string
                print(new_string, "max")
        return result


answer = Solution()
print(answer.sortString("aaaabbbbcccc"))


# retry
'''
class Solution_wrong:
    def sortString(self, s: str) -> str:
        s = list(s)
        new_string = ""
        whole_counter = len(s)

        def min_add(s_example, new_string_example):
            counter = 0
            while s_example:
                new_string_example += min(s_example)
                s_example.remove(min(s_example))
                counter += 1
            return new_string_example, counter, -1

        def max_add(s_example, new_string_example):
            counter = 0
            while s_example:
                new_string_example += max(s_example)
                s_example.remove(max(s_example))
                counter += 1
            return new_string_example, counter, 1

        turn = 1
        while whole_counter > 0:
            if turn == 1:
                new_string, count, turn = min_add(s, new_string)
                whole_counter -= count
                print(new_string, "min")
            elif turn == -1:
                new_string, count, turn = max_add(s, new_string)
                whole_counter -= count
                print(new_string, "max")
        return new_string
'''
