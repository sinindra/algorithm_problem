T = int(input())
for test_case in range(1, T + 1):
    a, b = map(str, input().split())
    A = a.replace(b, '!')

    print("#{} {}".format(test_case, len(A)))