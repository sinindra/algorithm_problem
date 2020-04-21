T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    i = 0
    while N > 1:
        N = int(N // 2)
        i += 1
    
    if i % 2 == 1:
        ans = "Alice"
    else:
        ans = "Bob"
    print(i, N)

    print("#{} {}".format(test_case, ans))