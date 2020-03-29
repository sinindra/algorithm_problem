def scale(left, right, n):
    global bells, visit, N, ans
    if left < right:
        return
    
    if n >= N:
        ans += 1
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            # scale(left + [bells[i]], right, n + 1)
            scale(left + bells[i], right, n + 1)
            visit[i] = 0

            visit[i] = 1
            # scale(left, right + [bells[i]], n + 1)
            scale(left, right + bells[i], n + 1)
            visit[i] = 0
        else:
            continue

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bells = list(map(int, input().split()))

    visit = [0] * N
    ans = 0

    scale(0, 0, 0)

    print("#{} {}".format(test_case, ans))