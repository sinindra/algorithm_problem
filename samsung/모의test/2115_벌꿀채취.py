def dfs(i, bascket, honey):
    global p, C, visit, M
    if i == M:
        tmp = sum([ x ** 2 for x in honey])
        if tmp > p:
            p = tmp
        return

    for k in range(M):
        if sum(honey) + bascket[k] <= C and visit[k] == 0:
            visit[k] = 1
            dfs(i+1, bascket, honey + [bascket[k]])
            visit[k] = 0
        elif visit[k] == 0:
            visit[k] = 1
            dfs(i+1, bascket, honey)
            visit[k] = 0


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    nest = [list(map(int, input().split())) for _ in range(N)]

    visit = [0] * M
    profit = [[0] * (N - M + 1) for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            p = 0
            dfs(0, nest[i][j:j+M], [])
            profit[i][j] = p

    ans = 0
    for i in range(N):
        for j in range(N - M + 1):
            tmp_a = profit[i][j]
            tmp_profit = profit[i][j:j+M]
            profit[i][j:j+M] = [0] * M

            if i == N-1:
                tmp_b = max([max(x + [0]) for x in profit[:i]])
                tmp_b = max(tmp_b, max(profit[i][j+M:] + [0]))
            else:
                tmp_b = max([max(x + [0]) for x in profit[i+1:]] + [0])
                tmp_b = max(tmp_b, max(profit[i][j+M:] + [0]))

            tmp = tmp_a + tmp_b
            if tmp > ans:
                ans = tmp
            profit[i][j:j+M] = tmp_profit

    print("#{} {}".format(test_case, ans))