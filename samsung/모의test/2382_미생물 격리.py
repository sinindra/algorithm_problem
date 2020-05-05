from collections import defaultdict

class Virus():
    def __init__(self, r, c, n, d):
        self.r = r
        self.c = c
        self.n = n
        self.d = d
        
        self.D = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

    def change(self):
        if self.d == 1:
            self.d = 2
        elif self.d == 2:
            self.d = 1
        elif self.d == 3:
            self.d = 4
        elif self.d == 4:
            self.d = 3

    def move(self):
        self.r, self.c = self.r + self.D[self.d][0], self.c + self.D[self.d][1]
        if self.r == 0 or self.r == N-1 or self.c == 0 or self.c == N-1:
            self.n = self.n // 2
            self.change()

def crash(A):
    global viruses
    A.sort(key = lambda x:x.n, reverse=True)
    while len(A) > 1:
        a = A.pop()
        A[0].n += a.n
        viruses.remove(a)

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    viruses = [Virus(*map(int, input().split())) for _ in range(K)]
    for m in range(M):
        grid = defaultdict(list)
        for v in viruses:
            v.move()
            grid[(v.r, v.c)].append(v)
        for g in grid.keys():
            if len(grid[g]) > 1:
                crash(grid[g])
    
    ans = 0
    for virus in viruses:
        ans += virus.n

    print("#{} {}".format(test_case, ans))