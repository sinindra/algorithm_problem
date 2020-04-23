def cal(op, A, B):
    if op == "+":
        return A + B
    elif op == "-":
        return A - B
    elif op == "*":
        return A * B
    elif op == "/":
        return int(A / B)

def dfs(i,tmp_sum):
    global N, ans_max, ans_min, OP, operator, nums
    if i == N:
        if tmp_sum > ans_max:
            ans_max = tmp_sum
        if tmp_sum < ans_min:
            ans_min = tmp_sum
        return

    for op in operator:
        if OP[op] > 0:
            OP[op] -= 1
            dfs(i+1, cal(op, tmp_sum, nums[i]))
            OP[op] += 1

T = int(input())
for test_case in range(1, T + 1):
    N =int(input())
    operator = ["+", "-", "*", "/"]
    num_op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    OP = dict(zip(operator, num_op))
    ans_max = float('-inf')
    ans_min = float('inf')
    dfs(1, nums[0])
    ans = ans_max - ans_min
    print("#{} {}".format(test_case, ans))