def dfs(i,tmp_sum):
    global N, ans_max, ans_min, nums, num_op
    if i == N:
        if tmp_sum > ans_max:
            ans_max = tmp_sum
        if tmp_sum < ans_min:
            ans_min = tmp_sum
        return

    for j in range(4):
        if num_op[j] > 0:
            num_op[j] -= 1
            if j == 0:
                tmp = tmp_sum + nums[i]
            elif j == 1:
                tmp = tmp_sum - nums[i]
            elif j == 2:
                tmp = tmp_sum * nums[i]
            elif j == 3:
                tmp = int(tmp_sum / nums[i])
            dfs(i+1, tmp)
            num_op[j] += 1

T = int(input())
for test_case in range(1, T + 1):
    N =int(input())
    num_op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    ans_max, ans_min = float('-inf'), float('inf')
    dfs(1, nums[0])
    ans = ans_max - ans_min
    print("#{} {}".format(test_case, ans))