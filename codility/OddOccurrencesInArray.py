#!/usr/bin/python

def solution(A):
    num = {}
    for i in A:
        if i in num:
            num[i] += 1
        else:
            num[i] = 1
    for i in list(num.keys()):
        if num[i] % 2 == 1:
            ans = i
            return ans

A = [42]

if __name__ == "__main__":
    print(solution(A))