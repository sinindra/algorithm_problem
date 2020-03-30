T = int(input())
for test_case in range(1, T + 1):
    N = input()
    count = 0
    if len(N) == 1:
        count = 0
    else:
        while len(N) >= 2:
            N = str(int(N[0]) + int(N[1])) + N[2:]
            count += 1
    if count % 2 == 0:
        ans = "B"
    else:
        ans = "A"
    print("#{} {}".format(test_case, ans))





