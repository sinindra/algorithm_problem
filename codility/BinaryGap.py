#!/usr/bin/python

def solution(N):
    b = str(format(N, 'b'))
    tmp, ans = 0, 0
    for i in b:
        if i == "0":
            tmp += 1
            
        elif i == "1":
            if tmp > ans:
                ans = tmp
            tmp = 0
        print(i, ans, tmp)        
    return b + " : " + str(ans)

N = 21564864

if __name__ == "__main__":
    print(solution(N))