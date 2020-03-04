def move(i, j):
    global grid, grid2
    n = 1
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = i, j
    c = True
    while c:
        for k in range(4):
            x2, y2 = x + d[k][0], y + d[k][1]
            if x2 < 0 or x2 >= N or y2 < 0 or y2 >= N:
                if k == 3:
                    c = False
                continue

            if int(grid[x2][y2]) == int(grid[x][y]) + 1:
                x, y = x2, y2
                if grid2[x][y] != 0:
                    n += grid2[x][y]
                    c = False
                    break
                else:
                    n += 1
                    break

            elif k == 3:
                c = False

    grid2[i][j] = n
    return

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    grid = [list(input().split()) for _ in range(N)]
    grid2 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            move(i, j)
    ans = [100000000, 0]
    for i in range(N):
        for j in range(N):
            if grid2[i][j] > ans[1]:
                ans = [int(grid[i][j]), grid2[i][j]]
            elif grid2[i][j] == ans[1] and int(grid[i][j]) < ans[0]:
                ans = [int(grid[i][j]), grid2[i][j]]
    print("#{} {} {}".format(test_case, ans[0], ans[1]))
