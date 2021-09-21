def solution(s):
    answer = -1

    if len(s) % 2 == 1:
        return 0

    stack = []

    for alpha in s:
        stack.append(alpha)
        while len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    slist = ['baabaa', 'cdcd']
    results = [1, 0]

    for s, result in zip(slist, results):
        print('->', solution(s), result)