def dfs(i, tmp_sum):
    global ans
    if i >= 12:
        if tmp_sum < ans:
            ans = tmp_sum
        return
    
    if i < 12:
        dfs(i+3, tmp_sum + fee[2])
        dfs(i+1, tmp_sum + fee_tmp[i])

T = int(input())
for test_case in range(1, T + 1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    fee_tmp = [min(fee[0] * use, fee[1]) for use in plan]
    
    ans = float('inf')
    dfs(0, 0)
    if ans > fee[-1]:
        ans = fee[-1]

    print("#{} {}".format(test_case, ans))