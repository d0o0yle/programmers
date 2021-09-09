import heapq

def solution(scoville, K):
    answer = 0

    # qScoville = []
    # heapq.heapify(scoville) -> 이렇게도 쓸수있대
    # for aScoville in sorted(scoville):
    #     heapq.heappush(qScoville, aScoville)

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        answer += 1

    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    result = 2
    print('->', solution(scoville, K), result)