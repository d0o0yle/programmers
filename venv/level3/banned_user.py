from itertools import product


def solution(user_id, banned_id):
    answer = ""
    banned_list = dict()
    for aBannedId in banned_id:
        banned_list[aBannedId] = set()
    for aUserId in user_id:
        for aBannedId in banned_id:
            flag = True
            if len(aUserId) != len(aBannedId):
                continue
            for aCharUserId, aCharBannedId in zip(aUserId, aBannedId):
                if aCharBannedId not in ['*', aCharUserId]:
                    flag = False
            if flag:
                banned_list[aBannedId].add(aUserId)

    product_list = list()
    for aBannedId in banned_id:
        product_list.append(banned_list[aBannedId])

    answers = []

    for _product in list(product(*product_list)):
        oriLength = len(_product)
        newSet = set(_product)
        newLength = len(newSet)

        if oriLength != newLength:
            continue

        if newSet not in answers:
            answers.append(newSet)

    return len(answers)

if __name__ == "__main__":
    user_ids = [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["frodo", "fradi", "crodo", "abc123", "frodoc"]]
    banned_ids = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]
    results = [2, 2, 3]

    for user_id, banned_id, result in zip(user_ids, banned_ids, results):
        print("--")
        print(solution(user_id, banned_id), result)
        print("--")
