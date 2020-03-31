def count(N):
    if N > 0:
        count = 0
        N_str = str(N)[::-1]
        for i in range(len(N_str)):
            if int(N_str[i]) >= 4:
                N_tmp = int(N_str[i]) - 1
            else:
                N_tmp = int(N_str[i])
            if i > 0:
                diff = [(10 ** j) * (9 ** (i - j - 1)) for j in range(i)]
                count += N_tmp * ((10 ** i) - sum(diff))
            else:
                count += N_tmp
    return count    


T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A > 0 and B > 0:
        ans = count(B) - count(A)

    elif A < 0 and B > 0:
        ans = count(B) + count(abs(A)) - 1

    elif A < 0 and B < 0:
        ans = count(abs(A)) - count(abs(B))

    print("#{} {}".format(test_case, ans))
