#!/usr/bin/python

def solution(A, B, K):
    mb = int(B // K)
    ma = int(A // K)
    
    if A % K == 0:
        ans = mb - ma + 1
    else:
        ans = mb - ma
    return ans


A = 1
B = 2
K = 3

if __name__ == "__main__":
    print(solution(A, B, K))
