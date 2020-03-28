#!/usr/bin/python

def solution(S, P, Q):
    ans = [0] * len(P)
    for i in range(len(P)):
        word = S[P[i]:Q[i] + 1]
        if "A" in word:
            ans[i] = 1
            continue
        elif "C" in word:
            ans[i] = 2
            continue
        elif "G" in word:
            ans[i] = 3
            continue
        elif "T" in word:
            ans[i] = 4
            continue
    return ans


A = "ACGT"
B = []
K = []

if __name__ == "__main__":
    print(solution(S, P, Q))
