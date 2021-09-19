from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []

    for courseNum in course:
        orderCount = dict()
        tempAnswer = []
        maxValue = 2
        menus = []
        for order in orders:
            tempList = list(combinations(list(order), courseNum))
            for temp in tempList:
                menus.append(''.join(sorted(temp)))
        mostOrdered = Counter(menus).most_common()
        if len(mostOrdered) == 0:
            continue
        else:
            mostValue = mostOrdered[0][1]
            if mostValue == 1:
                continue
        for ordered in mostOrdered:
            if ordered[1] == mostValue:
                tempAnswer.append(ordered[0])
            else:
                break

            # for aTemp in tempList:
            #     temp = ''.join(sorted(aTemp))
            #     if temp not in orderCount:
            #         orderCount[temp] = 1
            #     else:
            #         orderCount[temp] += 1
        # for key, value in orderCount.items():
        #     if value > maxValue:
        #         maxValue = value
        #         tempAnswer.clear()
        #         tempAnswer.append(key)
        #     elif value == maxValue:
        #         tempAnswer.append(key)
        #     else:
        #         continue
        answer += tempAnswer

    return sorted(answer)

if __name__ == '__main__':
    ordersList = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
                  ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
                  ["XYZ", "XWY", "WXA"]]
    courses = [[2,3,4],
               [2,3,5],
               [2,3,4]]
    results = [["AC", "ACDE", "BCFG", "CDE"],
               ["ACD", "AD", "ADE", "CD", "XYZ"],
               ["WX", "XY"]]

    for orders, course, result in zip(ordersList, courses, results):
        print('->', solution(orders, course), result)