import math
from itertools import combinations

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    three_nums = list(combinations(nums, 3))
    for three_num in three_nums:
        if is_prime(sum(three_num)):
            answer += 1
    return answer

if __name__ == '__main__':
    numsList = [[1,2,3,4], [1,2,7,6,4]]
    results = [1,4]
    for nums, result in zip(numsList, results):
        print(solution(nums), result)