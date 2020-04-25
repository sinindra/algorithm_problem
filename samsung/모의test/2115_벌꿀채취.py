def pay(A):
    pay = 0
    for i in range(1, 1 << M):
        honey = 0
        tmp_pay = 0
        for j in range(M):
            if i & (1 << j):
                honey += A[j]
                tmp_pay += A[j] ** 2
        if honey <= C and tmp_pay > pay:
            pay = tmp_pay
    return pay

    
T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    nest = [list(map(int, input().split())) for _ in range(N)]

    profit = []
    for i in range(N):
        for j in range(N - M + 1):
            profit.append(pay(nest[i][j:j+M]))
        for j in range(N - M + 1, N):
            profit.append(0)

    ans = 0
    for i in range(len(profit) - M):
        for j in range(i+M, len(profit)):
            ans = max(ans, profit[i] + profit[j])
            
    print("#{} {}".format(test_case, ans))