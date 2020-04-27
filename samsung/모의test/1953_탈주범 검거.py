from collections import deque

pipe_next = {0:[1, 2, 5, 6], 1:[1, 3, 6, 7], 2:[1, 2, 4, 7], 3:[1, 3, 4, 5]}
pipe = {1: [0, 1, 2, 3],
        2: [0, 2], 
        3: [1, 3], 
        4: [0, 1], 
        5: [1, 2], 
        6: [2, 3], 
        7: [3, 0]}
direction1 = [-1, 0, 1, 0]
direction2 = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = 1
    que = deque([(R, C, 1)])
    ans = 0
    while que:
        x1, y1, t = que.popleft()
        if t > L:
            break
        ans += 1
        current_pipe = grid[x1][y1]
        for i in pipe[current_pipe]:
            x2, y2 = x1 + direction1[i], y1 + direction2[i]
            if x2 < 0 or x2 >= N or y2 < 0 or y2 >= M:
                continue
            tmp_pipe = grid[x2][y2]
            if tmp_pipe in pipe_next[i] and visit[x2][y2] == 0:
                que.append((x2, y2, t+1))
                visit[x2][y2] = 1
        
    print("#{} {}".format(test_case, ans))