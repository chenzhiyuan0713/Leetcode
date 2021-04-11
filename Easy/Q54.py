"""
1002. 查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]

"""


class Solution2:
    def commonChars(self, A):
        result = list(A[0])
        for each_word in A:
            for each_char_in_result in result:
                cache = list(each_word)
                if each_char_in_result not in each_word:
                    result.remove(each_char_in_result)
                if each_char_in_result in each_word:
                    cache.remove(each_char_in_result)
                    each_word = "".join(cache)
        return result


class Solution:
    def commonChars(self, A):
        result = []
        final_result_list = [0] * 26
        output_list = []
        for each_word in A:
            counter_list = [0] * 26
            for each_char in each_word:
                counter_list[ord(each_char)-97] += 1
            result.append(counter_list)
        for j in range(26):
            final_result_list[j] = min(result[i][j] for i in range(len(A)))
        turn_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for index in range(26):
            output_list += turn_list[index] * final_result_list[index]
        return output_list


answer = Solution()
# print(answer.commonChars(["bella","label","roller"]))
print(answer.commonChars(["daaccccd","adacbdda","abddbaba","bacbcbcb","bdaaaddc","cdadacba","bacbdcda","bacdaacd"]))