class Solution:
    def interpret(self, command: str) -> str:
        command_list = list(command)
        new_list = []
        for index in range(len(command_list)):
            if command_list[index] ==  "G":
                new_list.append("G")
                continue
            elif command_list[index] == "(":
                if command_list[index+1] == ")":
                    new_list.append("o")
                    index += 1
                    continue
                else:
                    new_list.append("al")
                    index += 3
        return "".join(new_list)


answer = Solution()
print(answer.interpret("(al)G(al)()()G"))
