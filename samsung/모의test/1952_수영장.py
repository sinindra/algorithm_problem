T = int(input())
for test_case in range(1, T + 1):
    prices= list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(dp[i-1] + prices[0] * plan[i-1], dp[i-1] + prices[1])
        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + prices[2])
    if dp[-1] > prices[-1]:
        dp[-1] = prices[-1]
    ans = dp[-1]

    print("#{} {}".format(test_case, ans))