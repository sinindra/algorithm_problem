#!/usr/bin/python

def solution(A):
    visit = [0] * 1000000
    for num in A:
        if num <= 0:
            continue
        else:
            if visit[num-1] == 0:
                visit[num-1] = 1
    idx = 0
    for v in visit:
        if v == 0:
            return idx + 1
        idx += 1

    return idx + 1




if __name__ == "__main__":
    print(solution(A))