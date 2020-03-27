#!/usr/bin/python

def solution(A):
    if len(A) == 0:
        return 1
        
    A.sort()
    
    if A[-1] == len(A):
        return len(A) + 1
    
    for i in range(len(A)):
        if i + 1 != A[i]:
            return i + 1


if __name__ == "__main__":
    print(solution(A))