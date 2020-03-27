#!/usr/bin/python

def solution(X, A):
    leaf = [0] * X
    bridge = 0
    for i in range(len(A)):
        if leaf[A[i]] == 0:
            leaf[A[i]] = 1
            bridge += 1
            if bridge == X:
                return i
    return -1


A = (5, [1, 3, 1, 4, 2, 3, 5, 4])

if __name__ == "__main__":
    print(solution(A))