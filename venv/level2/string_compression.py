def solution(s):
    answer = ""
    maxLen = len(s) // 2
    print(maxLen)
    answers = []

    if len(s) == 1:
        return 1

    for unit in range(1, maxLen + 1):
        compStr = ""
        cutStr = s[:unit]
        count = 1
        for i in range(unit, len(s), unit):
            tempStr = s[i:i+unit]

            if cutStr == tempStr:
                count += 1
            else:
                if count == 1:
                    compStr += cutStr
                else:
                    compStr += str(count) + cutStr
                cutStr = tempStr
                count = 1

        if count == 1:
            compStr += tempStr
        else:
            compStr += str(count) + cutStr
        answers.append(len(compStr))
    return min(answers)

if __name__ == "__main__":
    s_list = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
    results = [7, 9, 8, 14, 17]
    for s, result in zip(s_list, results):
        print("->", solution(s), result)