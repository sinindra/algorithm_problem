T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    P = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        P[a].append(b)
        P[b].append(a)
        
    visit = [True] * (N + 1)
    visit[0] = False
    ans = 0

    for i in range(1, N + 1):
        if visit[i]:
            que = P[i]
            while que:
                tmp = que.pop(0)
                if visit[tmp]:
                    visit[tmp] = False
                    que.extend(P[tmp])
            ans += 1

    print("#{} {}".format(test_case, ans))
