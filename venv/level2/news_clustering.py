import re

def filter_alpha(aString):
    p = re.compile('[A-Za-z]{2}')
    substrList = []
    results = []
    for i in range(len(aString)-2):
        substrList.append(aString[i:i+2])
    substrList.append(aString[-2:])

    for substr in substrList:
        isMatch = p.match(substr)
        if isMatch:
            results.append(substr.upper())
        else:
            continue
    return results

def solution(str1, str2):
    substr1List = filter_alpha(str1)
    substr2List = filter_alpha(str2)
    lenAll = len(substr1List) + len(substr2List)

    if lenAll == 0:
        return 65536

    intersection = 0

    for substr1 in substr1List:
        if substr1 in substr2List:
            intersection += 1
            substr2List.remove(substr1)

    union = lenAll - intersection

    answer = int(intersection * 65536 / union)

    return answer

if __name__ == '__main__':
    str1List = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2']
    str2List = ['french', 'shake hands', 'AAAA12', 'e=m*c^2']
    answers = [16384, 65536, 43690, 65536]



    for str1, str2, answer in zip(str1List, str2List, answers):
        print('->', solution(str1, str2), answer)