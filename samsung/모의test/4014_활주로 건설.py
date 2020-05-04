def check(A):
    d = 0
    must_d = 0
    down = 0
    here = A[0]
    for j, i in enumerate(A):
        road = i
        h = road - here
        if h == 0:
            d += 1
            if down == 1:
                must_d += 1
                if j == len(A) - 1 and d < X:
                    return 0
        
        elif h == 1:  #올라갈때
            if down == 1:
                if must_d < 2*X:
                    return 0
                down = 0
                must_d = 0
                d = 1
            else:
                if d < X:
                    return 0
                d = 1
                
        elif h == -1: #내려갈때
            if down == 1:
                if d < X:
                    return 0
                must_d = 1
                d = 1
            else:
                down = 1
                must_d = 1
                d = 1
            if j == len(A) - 1 and X > 1:
                return 0

        elif abs(h) > 1:
            return 0
        
        here = road
    return 1

T = int(input())
for test_case in range(1, T + 1):
    N, X = map(int, input().split())
    airstrip = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        tmp = [airstrip[j][i] for j in range(N)]
        airstrip.append(tmp)
    
    ans = 0
    for A in airstrip:
        ans += check(A)

    print("#{} {}".format(test_case, ans))