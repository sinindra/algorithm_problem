class Customer(object):
    def __init__(self, i, t, start=None, end=None, A=None, B=None):
        self.i = i
        self.t = t
        self.start = start
        self.end = end
        self.A = A
        self.B = B

T = int(input())
for test_case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    customers = list(map(int, input().split()))
    wait_rec = [Customer(i+1, t) for i, t in enumerate(customers)]
    print(wait_rec)
    wait_rep = []
    fin = []
    rec, rep = [0] * N, [0] * M
    t = 0

    while len(fin) < K:
        for i in range(N):
            if rec[i] == 0 and wait_rec:
                if t >= wait_rec[0].t:
                    C = wait_rec.pop(0)
                    C.start, C.end, C.A = t, t+As[i], i+1
                    rec[i] = C
            elif rec[i] != 0:
                C = rec[i]
                print(C.end)
                if t >= C.end:
                    C.start, C.end = None, None
                    wait_rep.append(C)
                    rec[i] = 0
                    if wait_rec:
                        if t >= wait_rec[0].t:
                            C = wait_rec.pop(0)
                            C.start, C.end, C.A = t, t+As[i], i+1
                            print(C.start, C.end)
                            rec[i] = C
        print("rec", t, wait_rec, rec)                            

        if wait_rep or rep != [0] * M:
            for j in range(M):
                if rep[j] == 0:
                    if wait_rep:
                        C = wait_rep.pop(0)
                        C.start, C.end, C.B = t, t+Bs[j], j+1
                        print(C.start, C.end)
                        rep[j] = C
                else:
                    C = rep[j]
                    if t >= C.end:
                        fin.append(C)
                        rep[j] = 0
                        if wait_rep:
                            C = wait_rep.pop(0)
                            C.start, C.end, C.B = t, t+Bs[j], j+1
                            rep[j] = C
        print("rep", t, wait_rep, rep)                            
        
        print(fin)
        t += 1
        input()
    ans = 0
    for k in fin:
        if k.A == A and k.B == B:
            ans += k.i
    
    if ans == 0:
        ans = -1

    print("#{} {}".format(test_case, ans))