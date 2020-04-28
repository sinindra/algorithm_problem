import copy

def bid(grid, w):
    for i in range(H):
        if grid[i][w] == 0:
            continue
        else:
            return (i, w)
    return

def chain(grid, bid_r, bid_c, bid_s, score):
    grid2 = grid
    count = 0
    visit = [[0] * W for _ in range(H)]
    stack = [(bid_r, bid_c, bid_s)]
    while stack:
        r, c, s = stack.pop()
        visit[r][c] = 1
        grid2[r][c] = 0
        count += 1
        for i in range(4):
            for j in range(1, s):
                rr, cc = r + (j * d[i][0]), c + (j * d[i][1])
                if rr < 0 or rr >= H or cc < 0 or cc >= W:
                    break
                if visit[rr][cc] == 0 and grid2[rr][cc] != 0:
                    visit[rr][cc] = 1
                    stack.append((rr, cc, grid[rr][cc]))
    
    for i in range(W):
        for j in range(H)[::-1]:
            if grid2[j][i] == 0:
                for k in range(j)[::-1]:
                    if grid2[k][i] == 0:
                        continue
                    else:
                        grid2[j][i], grid2[k][i] = grid2[k][i], 0
                        break
    return (grid2, score - count)

def dfs(n, grid, remain, o):
    global ans
    if n == N:
        if remain < ans:
            ans = remain
        return
    
    for i in range(W):
        tmp_bid = bid(grid, i)
        if tmp_bid:
            grid2, tmp_remain = chain(copy.deepcopy(grid), tmp_bid[0], tmp_bid[1], grid[tmp_bid[0]][tmp_bid[1]], remain)
            dfs(n+1, grid2, tmp_remain, o+str(i))
        else:
            dfs(n+1, grid, remain, o+str(i))
        


T = int(input())
for test_case in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    total = 0
    
    for i in range(H):
        for j in range(W):
            if grid[i][j] != 0:
                total += 1

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = 10000
    dfs(0, grid, total, "")
        
    print("#{} {}".format(test_case, ans))