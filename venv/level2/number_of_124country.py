def solution(n):
    answer = ''

    dict124 = {0: '1', 1: '2', 2: '4'}

    q, r = divmod(n-1, 3)

    answer += dict124[r]
    while q > 0:
        q -= 1
        answer = dict124[q % 3] + answer
        q = q // 3


    return answer

if __name__ == "__main__":
    nList = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    results = [1,2,4,11,12,14,21,22,24,41,42,44,111]
    for n, result in zip(nList, results):
        print('->', solution(n), result)