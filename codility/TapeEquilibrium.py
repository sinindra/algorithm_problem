#!/usr/bin/python

def solution(A):
    M = sum(A)
    left = [0] * (len(A))
    right = [0] * (len(A))
    for i in range(1, len(A)):
        left[i] = left[i-1] + A[i-1]
        right[i] = abs(M - 2 * left[i])

    return min(right[1:])


A = [3, 1, 2, 4, 3]

if __name__ == "__main__":
    print(solution(A))