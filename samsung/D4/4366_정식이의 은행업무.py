def search():
    global p_A, p_B, n_A, n_B

    for i in p_A:
        for j in p_B:
            if n_A + i == n_B +j:
                ans = n_A + i
                return ans

T = int(input())
for test_case in range(1, T + 1):
    A = input()
    B = input()
    n_A = int(A, 2)
    n_B = int(B, 3)
    p_A = []
    p_B = []
    idx = 0
    for i in A[::-1]:
        if i == "1":
            p_A.append(-1 * 2 ** idx)
        if i == "0":
            p_A.append(2 ** idx)
        idx += 1
    p_A.append(2 ** idx)

    idx = 0
    for i in B[::-1]:
        if i == "0":
            p_B.append(3 ** idx)
            p_B.append(2 * 3 ** idx)
        if i == "1":
            p_B.append(-1 * 3 ** idx)
            p_B.append(3 ** idx)
        if i == "2":
            p_B.append(-1 * 3 ** idx)
            p_B.append(-2 * 3 ** idx)
        idx += 1
    p_B.extend([3 ** idx, 2 * 3 ** idx])

    ans = search()

    print("#{} {}".format(test_case, ans))