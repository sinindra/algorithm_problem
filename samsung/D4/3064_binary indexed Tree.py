class BIT(object):
    def __init__(self, N, nums):
        self.n = N
        self.nums = nums
        self.tree = [0] * (N + 1)
        
        order = 0
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.tree[k] += self.nums[i]
                k += (k & -k)

    def update(self, idx, num):
        k = idx
        while k <= self.n:
            self.tree[k] += num
            k += (k & -k)

    def get(self, idx):
        k = idx
        sum = 0
        while k > 0:
            sum += self.tree[k]
            k -= (k & -k)
        return sum

    def range_sum(self, start, end):
        if start == 1:
            return str(self.get(end))
        else:
            return str(self.get(end) - self.get(start-1))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    B = BIT(N, nums)
    ans = []
    for i in range(M):
        C, X, Y = map(int, input().split())
        if C == 1:
            B.update(X, Y)
        if C == 2:
            ans.append(B.range_sum(X, Y))
    print("#{} {}".format(test_case, " ".join(ans)))
