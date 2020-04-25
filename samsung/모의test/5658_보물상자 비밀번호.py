number = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()
    num_list = []
    span = int(N/4)
    for _ in range(span):
        num_list.extend([nums[i:i + span] for i in range(0, N, span)])
        nums = nums[1:] + nums[0]
    
    num_list = list(set(num_list))
    num_list.sort(reverse=True)
    ans = sum([(16 ** i) * number[n] for i, n in enumerate(num_list[K-1][::-1])])

    print("#{} {}".format(test_case, ans))