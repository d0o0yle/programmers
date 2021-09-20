def solution(s):
    answer = []

    tuples = s[2:-2].split('},{')
    tuples.sort(key=len)

    for tup in tuples:
        tup = tup.split(',')
        answer.append((set(tup)-set(answer)).pop())

    return list(map(int, answer))

if __name__ == '__main__':
    slist = ["{{2},{2,1},{2,1,3},{2,1,3,4}}",
             "{{1,2,3},{2,1},{1,2,4,3},{2}}",
             "{{20,111},{111}}",
             "{{123}}",
             "{{4,2,3},{3},{2,3,4,1},{2,3}}"]
    results = [[2, 1, 3, 4],
               [2, 1, 3, 4],
               [111, 20],
               [123],
               [3, 2, 4, 1]]

    for s, result in zip(slist, results):
        print('->', solution(s), result)