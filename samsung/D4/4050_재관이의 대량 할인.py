T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))
    L = sorted(L, reverse=True)
    ans = 0
    for i in range(N):
        if (i + 1) % 3 == 0:
            continue
        else:
            ans += L[i]

    print("#{} {}".format(test_case, ans))