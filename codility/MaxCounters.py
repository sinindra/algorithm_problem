#!/usr/bin/python

def solution(N, A):
    counter = [0] * N
    c_max = 0
    max_counter = c_max
    for x in A:
        if x == N + 1:
            if c_max > max_counter:
                counter = [c_max] * N
                max_counter = c_max
            
        else:
            counter[x - 1] += 1
            if counter[x - 1] > c_max:
                c_max = counter[x - 1]
    
    return counter


N, A = 5, [3, 4, 4, 6, 1, 4, 4]

if __name__ == "__main__":
    print(solution(N, A))