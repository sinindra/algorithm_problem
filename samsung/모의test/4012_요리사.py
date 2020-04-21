def score(A):
    global S, N
    s1, s2 = 0, 0
    B = list(set(range(N)) - set(A))
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            s1 += S[A[i]][A[j]]
            s1 += S[A[j]][A[i]]
    
    for i in range(len(B) - 1):
        for j in range(i + 1, len(B)):
            s2 += S[B[i]][B[j]]
            s2 += S[B[j]][B[i]]
    return abs(s1 - s2)

def dfs(F, i):
    global S, ans, n
    
    if len(F) == n:
        tmp = score(F)
        if tmp < ans:
            ans = tmp
        return
    
    if i == N:
        return
    if len(F) < n:
        dfs(F + [i], i + 1)
        dfs(F, i + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n = int(N/2)
    S = [ list(map(int, input().split())) for _ in range(N) ]
    ans = float("inf")
    dfs([], 0)
    print("#{} {}".format(test_case, ans))