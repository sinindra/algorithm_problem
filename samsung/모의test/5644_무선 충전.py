class Map():
    def __init__(self, path_A, path_B, BC):
        self.A = (1,1)
        self.B = (10,10)
        self.path_A = path_A
        self.path_B = path_B
        
        self.map = {}
        for i, (x, y, c, p) in enumerate(BC):
            for j in range(-c, c+1):
                for k in range(-c, c+1):
                    if abs(j) + abs(k) <= c:
                        tmp = (x + j, y + k)
                        if tmp in self.map:
                            self.map[tmp].append((i, p))
                        else:
                            self.map[tmp] = [(i, p)]

        self.d = [(0,0), (0, -1), (1, 0), (0, 1), (-1, 0)]

    def update(self, i):
        self.A = (self.A[0] + self.d[path_A[i]][0], self.A[1] + self.d[path_A[i]][1])
        self.B = (self.B[0] + self.d[path_B[i]][0], self.B[1] + self.d[path_B[i]][1])

    def score(self):
        bc_A, bc_B = [], []
        if self.A in self.map:
            bc_A = self.map[self.A]
        if self.B in self.map:
            bc_B = self.map[self.B]
        
        bc_A = set(bc_A)
        bc_B = set(bc_B)
        bc_total = bc_A | bc_B

        if len(bc_total) == 0:
            return 0

        elif len(bc_total) == 1:
            return list(bc_total)[0][1]
        
        elif len(bc_A) + len(bc_B) == len(bc_total):
            bc_A = list(bc_A)
            bc_A.sort(key = lambda x:x[1])
            bc_B = list(bc_B)
            bc_B.sort(key = lambda x:x[1])
            if len(bc_A) == 0:
                return bc_B[-1][1]
            if len(bc_B) == 0:
                return bc_A[-1][1]
            return bc_A[-1][1] + bc_B[-1][1]
        
        else:
            bc_A = list(bc_A)
            bc_A.sort(key = lambda x:x[1])
            bc_B = list(bc_B)
            bc_B.sort(key = lambda x:x[1])
            if len(bc_total) == 2:
                bc_total = list(bc_total)
                ans_tmp = bc_total[0][1] + bc_total[1][1]

            elif bc_A[-1] == bc_B[-1]:
                if len(bc_A) == 1:
                    ans_tmp = bc_A[-1][1] + bc_B[-2][1]
                elif len(bc_B) == 1:
                    ans_tmp = bc_A[-2][1] + bc_B[-1][1]
                else:
                    ans_tmp = bc_A[-1][1] + max(bc_A[-2][1], bc_B[-2][1])
            
            else:
                ans_tmp = bc_A[-1][1] + bc_B[-1][1]
            return ans_tmp
        
    def play(self, M):
        ans = 0
        n = 0
        ans += self.score()
        while n < M:
            self.update(n)
            ans += self.score()
            n += 1

        return ans

T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    path_A = list(map(int, input().split()))
    path_B = list(map(int, input().split()))
    BC = [tuple(map(int, input().split())) for _ in range(A)]
    board = Map(path_A, path_B, BC)
    ans = board.play(M)

    print("#{} {}".format(test_case, ans))