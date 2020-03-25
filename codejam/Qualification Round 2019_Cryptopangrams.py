def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return abs(a)

alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

T = int(input())
for case in range(1, T + 1):
    N, L = map(int, input().split())
    nums = list(map(int, input().split()))
    # print(len(nums))

    prime = []
    S = [0] * (L + 1)
    que = []

    for i in range(1, L):
        # print(i, end=",")
        # print(nums[i-1], nums[i])
        tmp = gcd(nums[i-1], nums[i])
        if nums[i-1] == nums[i]:
            que.append(i)
            continue
        elif nums[i-1] % 2 == 0 and nums[i] % 2 == 0:
            S[i] = 2
        elif nums[i-1] % 2 != 0 and nums[i] % 2 == 0:
            S[i-1] = 2
        elif nums[i-1] % 2 == 0 and nums[i] % 2 != 0:
            S[i+1] = 2

        S[i] = tmp

    # print(que)
    # print(S)

    while que:
        idx = que.pop(0)

        if S[idx + 1] != 0:
            S[idx] = int(nums[idx] / S[idx + 1])
            continue
        elif S[idx - 1] != 0:
            S[idx] = int(nums[idx - 1] / S[idx - 1])
            continue
        else:
            que.append(idx)

    S[0] = int(nums[0] / S[1])
    S[-1] = int(nums[-1] / S[-2])
    
    prime = sorted(list(set(S)))

    A = {}
    for i in range(26):
        A[prime[i]] = alpha[i]
    # print(A)

    ans = ""
    # print(len(S), S)
    for s in S:
        ans += A[s]
    
    print("Case #{}: {}".format(case, ans))