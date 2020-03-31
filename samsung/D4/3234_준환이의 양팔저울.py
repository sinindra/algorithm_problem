def scale(left, right, n):
    global bells, visit, N, ans, S, P
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

            if P[i] == 1:
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
    S = sum(bells)
    visit = [0] * N
    P = [0 if bells[i] * 2 > S else 1 for i in range(N)]
    ans = 0
    
    print(P)

    scale(0, 0, 0)

    print("#{} {}".format(test_case, ans))




def dfs(k, state, left, right): 
    if left < right:
        return 0
    if k == N :
        return 1
     
    if dp[state] != -1:
        return dp[state]
     
    sum = 0 
    for i in range(N):
        if visit[i] == 0 :
            visit[i] = 1
            sum += dfs(k+1, state + mul[i], left + data[i], right)
            sum += dfs(k+1, state + mul[i] * 2, left, right + data[i])
            visit[i] = 0
  
    dp[state] = sum
    return sum
  
T = int(input())
visit= [0] * 10
mul = [1,3,9,27,81,243,729,2187,6561]  # 3 ^ n 값들
 
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    dp = [-1] * 20000
    ans = dfs(0, 0, 0, 0)
    print("#%d %d" %(tc+1, ans))