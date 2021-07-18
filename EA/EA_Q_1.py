def solution(card: list, word: list) -> list:
    # all_char_in_card = ("").join(card)
    # for each_word in word:

    pass_flag = 1
    answer = []
    reset = ("").join(card)

    for each_word in word:
        if len(each_word) > 10:
            continue

        flag1 = flag2 = flag3 = 0
        # flag2 = 0
        # flag3 = 0
        card = [reset[0:8], reset[8:16], reset[16:]]
        for each_char in each_word:
            if each_char in card[0]:
                flag1 = 1
                card[0] = card[0].replace(each_char, "", 1)
                # print(card)
                continue
            elif each_char in card[1]:
                flag2 = 1
                card[1] = card[1].replace(each_char, "", 1)
                continue
            elif each_char in card[2]:
                flag3 = 1
                card[2] = card[2].replace(each_char, "", 1)
                continue
            else:
                print("answer add nothing")
                flag1 = 0
                break

        if flag1 * flag2 * flag3 * pass_flag == 0:
            print("failed")
        else:
            answer.append(each_word)
    if not answer:
        return ["-1"]
    return answer


print(solution(["ABACDEFG","NOPQRSTU","HIJKLKMM"], ["GPQM", "GPMZ", "EFU", "MMNA"]))
# print(solution(["AABBCCDD","KKKKJJJJ","MOMOMOMO"], ["AAAKKKKKMMMMM", "ABCDKJ"]))