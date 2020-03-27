#!/usr/bin/python

def solution(X, Y, D):
    if X == Y:
        return 0
    
    delta = Y - X
    if D >= delta:
        return 1
    elif D == 1:
        return delta
    elif delta % D == 0:
        return int(delta / D)
    else:
        return int(delta // D) + 1


if __name__ == "__main__":
    print(solution(X, Y ,D))