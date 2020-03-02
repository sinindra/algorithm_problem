def play(i, j):
    global N, grid, safe
    d = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
    if grid[i][j] == '.':
        grid[i][j] = 0
        for x1, y1 in d:
            x, y = i + x1, j + y1
            if x < 0 or x >= N or y < 0 or y >= N or x == -1 or y == -1:
                continue
            if grid[x][y] == '*':
                grid[i][j] += 1

def play2(i, j):
    global N, grid, safe, sol
    d = [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)]
    que = [[i, j]]
    while que:
        i, j = que.pop(0)
        safe.remove([i, j])
        if grid[i][j] == 0:
            for x1, y1 in d:
                x, y = i + x1, j + y1
                if x < 0 or x >= N or y < 0 or y >= N or x == -1 or y == -1:
                    continue
                elif [x, y] in safe and [x, y] not in que:
                    que.append([x, y])

        else:
            nosafe = 1
            for x1, y1 in d:
                x, y = i + x1, j + y1
                if x < 0 or x >= N or y < 0 or y >= N or x == -1 or y == -1:
                    continue
                elif grid[x][y] == 0:
                    nosafe = 0

            if nosafe:
                continue
            else:
                for x1, y1 in d:
                    x, y = i + x1, j + y1
                    if x < 0 or x >= N or y < 0 or y >= N or x == -1 or y == -1:
                        continue
                    elif grid[x][y] == 0 and [x, y] in safe and [x, y] not in que:
                        que.append([x, y])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    grid = []
    safe = []
    for i in range(N):
        line = list(input())
        grid.append(line)
        for j in range(N):
            if line[j] == '.':
                safe.append([i, j])

    for i, j in safe:
        play(i, j)

    sol = 0
    while safe:
        sol += 1
        i, j = safe[0]
        play2(i, j)

    print("#{} {}".format(test_case, sol))