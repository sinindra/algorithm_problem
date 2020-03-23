T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []
    ans = 0
    for i in range(N):
        grid.append([0] * M)

    for i in range(N):
        for j in range(M):
            x, y = i + 2, j + 2
            if grid[i][j] == 0:
                if x < N:
                    if grid[x][j] == 0:
                        grid[x][j] = 1
                if y < M:
                    if grid[i][y] == 0:
                        grid[i][y] = 1
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                ans += 1
    
    print("#{} {}".format(test_case, ans))