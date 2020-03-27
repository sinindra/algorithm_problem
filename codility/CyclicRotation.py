#!/usr/bin/python

def solution(A, K):
    if len(A) == 0:
        return A
    if K == 0:
        return A

    if K < len(A):
        ans = A[-K:] + A[:-K]
    elif K % len(A) == 0:
        ans = A
    else:
        ans = A[-(K % len(A)):] + A[:-(K % len(A))]
    return ans

A = []
K = 10

if __name__ == "__main__":
    print(solution(A, K))