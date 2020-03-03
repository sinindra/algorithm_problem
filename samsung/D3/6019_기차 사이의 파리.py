T = int(input())
for test_case in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    t = D / (A + B)
    dist = 0
    dist = F * t
    print("#{} {}".format(test_case, dist))