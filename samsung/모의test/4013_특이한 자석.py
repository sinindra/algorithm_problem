from collections import deque

class Gear:
    def __init__(self, gear, s, direction= None, left=None, right=None):
        self.gear = gear
        self.left = left
        self.right = right
        self.s = s
        self.direction = direction

        self.u = self.gear[0]
        self.r = self.gear[2]
        self.l = self.gear[6]

    def rotate(self):
        self.gear.rotate(self.direction)
        self.u = self.gear[0]
        self.r = self.gear[2]
        self.l = self.gear[6]
        
    def score(self):
        return self.u * (2 ** self.s)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    gears = [Gear(deque(list(map(int, input().split()))), i) for i in range(4)]
    gears[0].right = gears[1]
    gears[1].left, gears[1].right = gears[0], gears[2]
    gears[2].left, gears[2].right = gears[1], gears[3]
    gears[3].left = gears[2]

    for i in range(N):
        move = [0] * 4
        visit = [0] * 4
        gear_num, direction = map(int, input().split())
        n = gear_num - 1
        gears[n].direction = direction

        que = [gears[n]]
        visit[n] = 1
        while que:
            tmp = que.pop()
            tmp_d = tmp.direction
            move[tmp.s] = 1
            visit[tmp.s] = 1

            if tmp.right:
                if tmp.r != tmp.right.l and visit[tmp.right.s] == 0:
                    tmp.right.direction = tmp.direction * (-1)
                    que.append(tmp.right)

            if tmp.left:
                if tmp.l != tmp.left.r and visit[tmp.left.s] == 0:
                    tmp.left.direction = tmp.direction * (-1)
                    que.append(tmp.left)

        for j in range(4):
            if move[j] == 1:
                gears[j].rotate()

    ans = sum([gears[i].score() for i in range(4)])

    print("#{} {}".format(test_case, ans))
    
"""
기어 객체 생성.
기어 좌,우 인접 기어 링크.
기어의 위,좌,우 정보를 갖고 있고, 객체는 기어 번호와 회전 방향을 갖고 있다.
stack을 통해 기어를 돌리고, 상황에 따라 인접 기어도 회전해야 할 경우 stack에 추가.
회전이 필요한 번호를 저장하고, 모든 기어 조사가 끝나면 일괄 회전.
회전을 하면 각 정보를 업데이트.
"""
