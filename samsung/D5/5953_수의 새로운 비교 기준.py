def nsum(s, N):
    ans = 0
    if len(s) != N:
        s = "0" * (N-len(s)) + s
    for i in s:
        ans += int(i)
    return ans

def prod(s, N):
    ans = 1
    if len(s) != N:
        s = "0" * (N-len(s)) + s
    for i in s:
        ans *= int(i) + 1
    return ans

def nint(s, N):
    ans = 0
    if len(s) != N:
        s = "0" * (N-len(s)) + s
    for i in s:
        N -= 1
        ans += int(i) * (10 ** N)
    return ans


T = int(input())
for test_case in range(1, T+1):
    s = input()
    N = len(s)
    sol = {}
    for i in range(10 ** N):
        i = str(i)
        sol[i] = (nsum(i,N), prod(i,N), nint(i,N))

    sol = sorted(sol.items(), key = (lambda x: x[1]))
    print(sol)
