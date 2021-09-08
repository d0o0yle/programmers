def solution(w,h):
    answer = 0
    if w == h:
        return w * h - h
    elif w == 1 or h == 1:
        return 0
    for x in range(w):
        answer += int(x*h/w)
    return answer * 2

if __name__ == "__main__":
    w, h, result = 8, 12, 80
    ws = [8,1,2]
    hs = [12,10,3]
    results = [80,0,2]

    for w, h, result in zip(ws, hs, results):
        print('->', solution(w, h), result)