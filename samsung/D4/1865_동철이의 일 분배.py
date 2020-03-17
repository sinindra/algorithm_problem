# def cal(n, S, O):
def cal(n, S):
    global P, ans, arr
    if n == N:
        sol = S
        # print(O)
        if S > ans:
            ans = sol
        return

    for i in range(N):
        if arr[i]:
            continue
        else:
            arr[i] = 1
            # cal(n + 1, S * P[n][i] * 0.01, O + [P[n][i]])
            cal(n + 1, S * P[n][i] * 0.01)
            arr[i] = 0        


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    arr = [0] * N
    for i in range(N):
        arr[i] = 1
        # cal(1, P[0][i] * 0.01, [P[0][i]])
        cal(1, P[0][i] * 0.01)
        arr[i] = 0
        
    print("#{} {}".format(test_case, round(ans * 100, 6)))