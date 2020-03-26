def play(d):
    global N, board, visit
    if d == "left":
        for i in range(N):
            for j in range(N):
                tmp = board[i][j]
                if tmp == 0:
                    continue
                next = j - 1
                while next >= 0:
                    if board[i][next] == 0:
                        if next == 0:
                            board[i][next] = tmp
                            board[i][j] = 0
                            break
                        next -= 1
                        continue

                    elif board[i][next] == tmp and visit[i][next] == 0:
                        board[i][next] = tmp * 2
                        board[i][j] = 0
                        visit[i][next] = 1
                        break

                    else:
                        board[i][j] = 0
                        board[i][next + 1] = tmp
                        break
    elif d == "right":
        for i in range(N):
            for j in range(N)[::-1]:
                tmp = board[i][j]
                if tmp == 0:
                    continue
                next = j + 1
                while next < N:
                    if board[i][next] == 0:
                        if next == N - 1:
                            board[i][next] = tmp
                            board[i][j] = 0
                            break
                        next += 1
                        continue

                    elif board[i][next] == tmp and visit[i][next] == 0:
                        board[i][next] = tmp * 2
                        board[i][j] = 0
                        visit[i][next] = 1
                        break

                    else:
                        board[i][j] = 0
                        board[i][next - 1] = tmp
                        break
    elif d == "up":
        for i in range(N):
            for j in range(N):
                tmp = board[j][i]
                if tmp == 0:
                    continue
                next = j - 1
                while next >= 0:
                    if board[next][i] == 0:
                        if next == 0:
                            board[next][i] = tmp
                            board[j][i] = 0
                            break
                        next -= 1
                        continue

                    elif board[next][i] == tmp and visit[next][i] == 0:
                        board[next][i] = tmp * 2
                        board[j][i] = 0
                        visit[next][i] = 1
                        break

                    else:
                        board[j][i] = 0
                        board[next + 1][i] = tmp
                        break
    elif d == "down":
        for i in range(N):
            for j in range(N)[::-1]:
                tmp = board[j][i]
                if tmp == 0:
                    continue
                next = j + 1
                while next < N:
                    if board[next][i] == 0:
                        if next == N - 1:
                            board[next][i] = tmp
                            board[j][i] = 0
                            break
                        next += 1
                        continue

                    elif board[next][i] == tmp and visit[next][i] == 0:
                        board[next][i] = tmp * 2
                        board[j][i] = 0
                        visit[next][i] = 1
                        break

                    else:
                        board[j][i] = 0
                        board[next - 1][i] = tmp
                        break

T = int(input())
for test_case in range(1, T + 1):
    N, d = map(str, input().split())
    N = int(N)
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    play(d)

    print("#{}".format(test_case))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()