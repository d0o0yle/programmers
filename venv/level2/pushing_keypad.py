def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solution(numbers, hand):
    answer = ''
    key_dict = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }

    left_side = [1, 4, 7]
    mid_side = [2, 5, 8, 0]
    right_side = [3, 6, 9]

    prev_left = (3, 0)
    prev_right = (3, 2)

    for number in numbers:
        if number in left_side:
            answer += 'L'
            prev_left = key_dict[number]
        elif number in right_side:
            answer += 'R'
            prev_right = key_dict[number]
        else:
            cur = key_dict[number]
            dist_left = distance(cur, prev_left)
            dist_right = distance(cur, prev_right)

            if dist_left < dist_right:
                answer += 'L'
                prev_left = cur
            elif dist_right < dist_left:
                answer += 'R'
                prev_right = cur
            else:
                if hand == "left":
                    answer += 'L'
                    prev_left = cur
                else:
                    answer += 'R'
                    prev_right = cur

    return answer

if __name__ == '__main__':
    numbersList = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    hands = ['right', 'left', 'right']
    results = ["LRLLLRLLRRL", "LRLLRRLLLRR", "LLRLLRLLRL"]

    for numbers, hand, result in zip(numbersList, hands, results):
        if solution(numbers, hand) == result:
            print(True)
        else:
            print(False)