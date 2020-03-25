T = int(input())
for test_case in range(1, T + 1):
    N = input()
    a, b = '', ''
    for num in N:
        if num == '4':
            a += '2'
            b += '2'
        else:
            a += num
            b += '0'
    print("Case #{}: {} {}".format(test_case, int(a), int(b)))
    